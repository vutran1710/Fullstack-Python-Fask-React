from threading import Thread
from flask import Flask, request
from services.logic import (
    make_file_path,
    convert_file_size,
    get_file_name,
    fix_file_name,
)
from models import (
    DataReport,
    GenDataAPIResponse,
    DataReportAPIResponse,
    StatusAPIResponse,
)
from utils import get_dependencies


app = Flask(__name__)


@app.route("/gen-data")
def generate_random_data():
    """Generate random data and write to file in the background
    Return file info
    """
    size = convert_file_size(request.args.get("size"))
    datagen, cache, fwriter, status = get_dependencies("dg", "ch", "fw", "st")
    path = make_file_path()
    report = DataReport()
    data_stream = datagen.generate_randoms(hook=report.update)

    def write_file_async():
        nonlocal fwriter, path, data_stream, size, report, status
        file_name = get_file_name(path)
        status.update_status(file_name, "WAITING")
        fwriter.write(path, data_stream, max_size=size)
        cache.save_data(file_name, report.dict())
        status.update_status(file_name, "FINISH")

    Thread(target=write_file_async).start()
    return GenDataAPIResponse(path=path, size=size).json()


@app.route("/check-status")
def check_file_write_status():
    """Return writing status for a specific file"""
    status = get_dependencies("st")
    name = fix_file_name(request.args.get("file"))
    stat = status.check_status(name)
    return StatusAPIResponse(file=name, status=stat).json() if stat else {}


@app.route("/data-report")
def get_file_report():
    """Get statistic report for a specific file
    API query-params:
    - file: file-name, either with extension or not
    Returns:
    - report data: dict
    """
    cache = get_dependencies("ch")
    file_name = fix_file_name(request.args.get("file"))
    result = cache.get_data(file_name)
    return DataReportAPIResponse(**result).json() if result else {}


if __name__ == "__main__":
    app.run()
