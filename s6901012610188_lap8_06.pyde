# ============================================================
# โปรแกรมที่ 2: วาดลูกโป่ง 5 ลูก โดยใช้ Class
# เก็บข้อมูลลูกโป่งทั้ง 5 ลูกในรูปแบบ Array ของ Object (Balloon)
# ============================================================

class Balloon:
    def __init__(self, x, y, size_val, r, g, b, speed):
        # Attributes ของลูกโป่ง 1 ลูก
        self.x = x
        self.y = y
        self.size_val = size_val
        self.r = r
        self.g = g
        self.b = b
        self.speed = speed

    def show(self):
        """Method สำหรับวาดลูกโป่งตามข้อมูลที่เก็บไว้ใน Attributes"""
        noStroke()
        fill(self.r, self.g, self.b)
        ellipse(self.x, self.y, self.size_val, self.size_val * 1.2)

        # แสงสะท้อนเล็กๆ บนลูกโป่ง
        fill(255, 255, 255, 120)
        ellipse(self.x - self.size_val * 0.2, self.y - self.size_val * 0.3,
                self.size_val * 0.25, self.size_val * 0.35)

        # ปมลูกโป่ง
        fill(self.r, self.g, self.b)
        triangle(self.x - 5, self.y + self.size_val * 0.6,
                  self.x + 5, self.y + self.size_val * 0.6,
                  self.x, self.y + self.size_val * 0.6 + 8)

        # เชือกลูกโป่ง
        stroke(80)
        strokeWeight(1)
        line(self.x, self.y + self.size_val * 0.6 + 8,
             self.x, self.y + self.size_val * 0.6 + 60)
        noStroke()

    def update(self):
        """อัพเดทตำแหน่งเพื่อทำ Animation ลอยขึ้น"""
        self.y -= self.speed
        if self.y < -100:
            self.y = height + 50


# Array (list) ของ Object Balloon ทั้ง 5 ลูก
# นักศึกษาสามารถกำหนดค่าเริ่มต้นเองได้
balloons = []


def setup():
    size(600, 600)
    background(255)

    global balloons
    balloons = [
        Balloon(100, 400, 60, 255, 0, 0, 1.5),
        Balloon(200, 450, 80, 0, 200, 0, 2.0),
        Balloon(300, 420, 50, 0, 100, 255, 1.2),
        Balloon(400, 480, 70, 255, 165, 0, 1.8),
        Balloon(500, 430, 65, 200, 0, 200, 1.0)
    ]


def draw():
    background(255)

    for b in balloons:
        b.show()      # วาดลูกโป่งตามข้อมูลใน Attributes
        b.update()     # อัพเดทตำแหน่งให้ลอยขึ้น
