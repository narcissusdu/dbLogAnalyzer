from app.DBLogAnalyzer import DBLogAnalyzer

if __name__ == '__main__':
    dbLogPath = r'e:\DB\db\Logs\16448 2017-12-27 02.05.txt'
    analyzer = DBLogAnalyzer(dbLogPath, 'en')
    analyzer.start()
