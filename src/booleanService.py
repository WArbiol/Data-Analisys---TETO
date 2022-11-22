class BooleanService:
    def isQuestion(column):
        identifier = column.split(' ')[0]
        numbers = identifier.split('.')
        hasInterrogation = False if len(column.split('?')) == 1 else True
        if (len(numbers) <= 1 and not hasInterrogation) or column.__contains__("(OBRIGATÓRIA"):
            return False
        else:
            return True

    def repeated(column, columns):
        # repeaeted column ends like .1 or .2
        if (column[-2] == '.'):
            return True
        index = columns.index(column)
        question = column.split('/')[0]
        if columns[index-1].__contains__(question):
            return True
        return False

    def hasMultipleOptions(column, columns):
        index = columns.index(column)
        if columns[index+1].__contains__(column):
            return True

        return False
