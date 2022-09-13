class OptionsService:
    def getAnswerOfTheOption(columnsOptions, df):
        dfOfOptions = df[columnsOptions]
        return dfOfOptions.sum().to_frame()

    def getTheColumnsWithOptions(column, columns):
        index = columns.index(column)
        options = []
        thereIsAnOption = True
        while thereIsAnOption:
            if columns[index+1].__contains__(column):
                option = columns[index+1].split('/')[-1]
                options.append(columns[index+1])
            else:
                thereIsAnOption = False
            index += 1
        return options
