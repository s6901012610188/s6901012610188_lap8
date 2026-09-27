class Matrix:
    def __init__(self, data):
        """
        data: list of lists เช่น [[1,2],[3,4]]
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def show(self):
        """แสดงผลเมทริกซ์"""
        for row in self.data:
            print(row)
        print()

    def add(self, other):
        """บวกเมทริกซ์ (ต้องมีขนาดเท่ากัน)"""
        if self.rows != other.rows or self.cols != other.cols:
            print("ขนาดเมทริกซ์ไม่เท่ากัน ไม่สามารถบวกได้")
            return None

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def subtract(self, other):
        """ลบเมทริกซ์ (ต้องมีขนาดเท่ากัน)"""
        if self.rows != other.rows or self.cols != other.cols:
            print("ขนาดเมทริกซ์ไม่เท่ากัน ไม่สามารถลบได้")
            return None

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def multiplication(self, other):
        """คูณเมทริกซ์ (จำนวนคอลัมน์ของตัวแรก ต้องเท่ากับจำนวนแถวของตัวที่สอง)"""
        if self.cols != other.rows:
            print("ขนาดเมทริกซ์ไม่สอดคล้องกัน ไม่สามารถคูณได้")
            return None

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)


# ---------------- ทดสอบโปรแกรม ----------------
if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])

    print("Matrix A:")
    A.show()

    print("Matrix B:")
    B.show()

    print("A + B =")
    result_add = A.add(B)
    result_add.show()

    print("A - B =")
    result_sub = A.subtract(B)
    result_sub.show()

    print("A x B =")
    result_mul = A.multiplication(B)
    result_mul.show()
