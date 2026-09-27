class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, amount):
        """อัปเดตจำนวนสินค้า เพิ่มหรือลดสต็อก"""
        if self.stock + amount < 0:
            print(f"[Error] สินค้า '{self.name}' มีไม่พอในสต็อก (คงเหลือ: {self.stock})")
            return False
        self.stock += amount
        print(f"[Success] อัปเดตสต็อก '{self.name}' สำเร็จ คงเหลือ: {self.stock}")
        return True

    def show_info(self):
        print(f"ID: {self.product_id} | Name: {self.name:<15} | Price: {self.price:>8.2f} THB | Stock: {self.stock:>4}")


class Inventory:
    def __init__(self):
        # จุดประสงค์ที่ 3: ใช้อาร์เรย์/List เก็บ Object
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_id):
        """ค้นหาสินค้าตาม ID"""
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None

    def show_all(self):
        print("\n--- รายการสินค้าทั้งหมดในคลัง ---")
        for p in self.products:
            p.show_info()


# --- ทดสอบการทำงาน ---
if __name__ == "__main__":
    inv = Inventory()
    inv.add_product(Product("P01", "Laptop", 25000, 5))
    inv.add_product(Product("P02", "Mouse", 550, 12))

    inv.show_all()

    # ทดสอบการค้นหาและอัปเดตสต็อก
    item = inv.find_product("P01")
    if item:
        item.update_stock(-2)  # ขายไป 2 ชิ้น
        item.update_stock(-10) # ลองตัดเกินสต็อกเพื่อทดสอบ Error Handling