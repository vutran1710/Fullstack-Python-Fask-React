from flask import Flask, request
from services.logic import make_file_path
from models import DataReport
from utils import get_dependencies

app = Flask(__name__)


@app.route("/gen-data")
def generate_data_and_save_to_file():
    dg, ch, fw = get_dependencies("dg", "ch", "fw")
    path = make_file_path()
    report = DataReport()
    data_stream = dg.generate_randoms(hook=report.update)
    file_info = fw.write(path, data_stream)
    ch.save_data(file_info.name, report.dict())
    return file_info.dict()


@app.route("/data-report")
def get_report_for_file():
    ch = get_dependencies("ch")
    file_name = request.args.get("file")
    return ch.get_data(file_name, dict())


if __name__ == "__main__":
    app.run()
