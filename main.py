import os
from flask import Flask, render_template, request, session, flash, jsonify, send_from_directory, redirect
from pychartjs import BaseChart, ChartType, Color
from decouple import config
import pandas as pd

def create_chart(x_column, y_column, data_frame):
    x_data = data_frame[x_column].tolist()
    
    if data_frame[y_column].dtype == 'O':
        y_data = data_frame[y_column].str.replace(',', '').astype(float).tolist()
    else:
        y_data = data_frame[y_column].tolist()

    class MyScatterChart(BaseChart):
        type = ChartType.Bar
        data = {
            'labels': x_data,
            'datasets': [{
                'label': y_column,
                'data': y_data,
                'backgroundColor': Color.Blue,
                'borderColor': Color.Blue,
                'fill': False,
                'pointRadius': 5,
                'pointHoverRadius': 8,
                'showLine': False
            }],
        }

    return MyScatterChart()

app = Flask(__name__)
app.secret_key = config('FLASK_SECRET_KEY')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_file', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)

    if file:
        if file.filename.endswith('.csv'):
            engine = 'python'
        elif file.filename.endswith(('.xlsx')):
            engine = None
        else:
            flash('Unsupported file format', 'error')
            return redirect(request.url)

        try:
            if engine == 'python':
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            columns = df.columns.tolist()

            session['file_data'] = df.to_json()
            return render_template('select_columns.html', columns=columns)

        except Exception as e:
            flash(f'Error reading file: {str(e)}', 'error')
            return redirect(request.url)

    return 'File processed successfully'
    
@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    x_column = request.form['x_column']
    y_column = request.form['y_column']

    if 'file_data' in session:
        data_frame = pd.read_json(session['file_data'])

        chart = create_chart(x_column, y_column, data_frame)

        return render_template('dashboards.html', chart=chart)
    else:
        return "Dados do arquivo não encontrados."

if __name__ == '__main__':
    app.run()