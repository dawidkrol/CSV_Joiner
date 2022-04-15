from Models.CSVmodel import CSV_model
from Models.CSVJoinTypes import JoinType


class CSVJoiner:

    def getColumnIDByName(self, model: CSV_model, column_name: str) -> int:
        return model.header.index(column_name)

    def add_columns(self, columnL: list[str], columnR: list[str], leftColumnId: int, rightColumnId: int) -> list[str]:
        output = []
        output.extend(columnL)
        for i, j in enumerate(columnR):
            if i != rightColumnId:
                output.append(j)
        return output

    def left_join(self, column_name: str, left: CSV_model, right: CSV_model):
        newLeft = CSV_model([], [])
        leftColumnID = self.getColumnIDByName(left, column_name)
        rightColumnID = self.getColumnIDByName(right, column_name)

        newLeft.header = self.add_columns(left.header, right.header, leftColumnID, rightColumnID)

        for l in left.data:
            isBroken = 0
            for r in right.data:
                if l[leftColumnID] == r[rightColumnID]:
                    newLeft.data.append(self.add_columns(l, r, leftColumnID, rightColumnID))
                    isBroken = 1
                    break
            if isBroken == 0:
                newLeft.data.append(l + ['' for i in range(len(right.data) - 2)])
        return newLeft

    def right_join(self, column_name: str, left: CSV_model, right: CSV_model):
        left, right = right, left
        return self.left_join(column_name, left, right)

    def inner_join(self, column_name: str, left: CSV_model, right: CSV_model):
        newLeft = CSV_model([], [])
        leftColumnID = self.getColumnIDByName(left, column_name)
        rightColumnID = self.getColumnIDByName(right, column_name)

        newLeft.header = self.add_columns(left.header, right.header, leftColumnID, rightColumnID)

        for l in left.data:
            for r in right.data:
                if l[leftColumnID] == r[rightColumnID]:
                    newLeft.data.append(self.add_columns(l, r, leftColumnID, rightColumnID))
                    break
        return newLeft

    def join(self, column_name: str, left: CSV_model, right: CSV_model, type: JoinType) -> CSV_model:
        if type == 1:
            return self.left_join(column_name, left, right)
        if type == 2:
            return self.right_join(column_name, left, right)
        if type == 3:
            return self.inner_join(column_name, left, right)
        return CSV_model([], [])
