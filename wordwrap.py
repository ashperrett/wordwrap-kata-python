class Wordwrap():

    def wrap(self,inStr,column):
        inStr = inStr.strip()
        if column == 0:
            return ""
        if len(inStr) <= column:
            return inStr.strip()
        elif len(inStr) > column:
            moveTo = column
            if inStr[column] != " ":
                moveTo = inStr.rfind(" ", 0, column)
            return inStr[:moveTo].strip() + "\n" + self.wrap(inStr[moveTo:],column).strip()
        return ""