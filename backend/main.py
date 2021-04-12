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
)
from utils import get_dependencies

app = Flask(__name__)


@app.route("/gen-data")
def generate_random_data():
    """Generate random data and save to file
    Return file-info data on success
    """
    size = convert_file_size(request.args.get("size"))
    datagen, cache, fwriter = get_dependencies("dg", "ch", "fw")
    path = make_file_path()
    report = DataReport()
    data_stream = datagen.generate_randoms(hook=report.update)

    def write_file_async(path, data_stream, max_size):
        file_info = fwriter.write(path, data_stream, max_size=size)
        cache.save_data(file_info.name, report.dict())

    t = Thread(target=write_file_async, args=(path, data_stream, size))
    t.start()
    return GenDataAPIResponse(path=path, size=size).json()


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
    result = cache.get_data(file_name, dict())

    if result:
        return DataReportAPIResponse(**result).json()

    return None


@app.route("/get-all")
def get_all_data():
    """
    debugging cache
    """
    cache = get_dependencies("ch")
    return cache.get_all()


if __name__ == "__main__":
    app.run()
