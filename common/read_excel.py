import xlrd
from read_config import ReadConfig

localConfig = ReadConfig()
filePath = localConfig.file_path('testfile', 'testfile.xlsx')


class ReadExcel:
    def read_excel(self, sheetname):
        cls = []
        excelFile = xlrd.open_workbook(filePath)
        sheet = excelFile.sheet_by_name(sheetname)
        nrows = sheet.nrows
        for nrow in range(nrows):
            if sheet.row_values(nrow)[0] != 'case_name':
                cls.append(sheet.row_values(nrow))
        return cls
