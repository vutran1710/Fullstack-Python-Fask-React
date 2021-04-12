from flask import Flask, request
from services.logic import make_file_path, convert_file_size
from models import DataReport
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
    file_info = fwriter.write(path, data_stream, max_size=size)
    cache.save_data(file_info.name, report.dict())
    return file_info.dict()


@app.route("/data-report")
def get_file_report():
    """Get statistic report for a specific file
    API query-params:
    - file: str
    Returns:
    - report data: dict
    """
    cache = get_dependencies("cache")
    file_name = request.args.get("file")
    return cache.get_data(file_name, dict())


if __name__ == "__main__":
    app.run()
