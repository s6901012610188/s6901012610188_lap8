# ============================================================
# โปรแกรมที่ 1: วาดลูกโป่ง 5 ลูก โดยไม่ใช้ Class
# เก็บข้อมูลด้วย Array/List
# ============================================================

num_balloons = 5

# เก็บข้อมูลลูกโป่งทั้ง 5 ลูกในรูปแบบ List
# นักศึกษาสามารถกำหนดค่าเริ่มต้นเองได้
x_pos = [100, 200, 300, 400, 500]
y_pos = [400, 450, 420, 480, 430]
sizes = [60, 80, 50, 70, 65]
colors = [
    (255, 0, 0),      # แดง
    (0, 200, 0),      # เขียว
    (0, 100, 255),    # ฟ้า
    (255, 165, 0),    # ส้ม
    (200, 0, 200)     # ม่วง
]
speeds = [1.5, 2.0, 1.2, 1.8, 1.0]


def setup():
    size(600, 600)
    background(255)


def draw_balloon(x, y, size_val, r, g, b):
    """ฟังก์ชันสำหรับวาดลูกโป่ง 1 ลูก ที่ตำแหน่ง (x, y)"""
    # ตัวลูกโป่ง
    noStroke()
    fill(r, g, b)
    ellipse(x, y, size_val, size_val * 1.2)

    # แสงสะท้อนเล็กๆ บนลูกโป่ง
    fill(255, 255, 255, 120)
    ellipse(x - size_val * 0.2, y - size_val * 0.3, size_val * 0.25, size_val * 0.35)

    # ปมลูกโป่ง (ล่างสุด)
    fill(r, g, b)
    triangle(x - 5, y + size_val * 0.6,
              x + 5, y + size_val * 0.6,
              x, y + size_val * 0.6 + 8)

    # เชือกลูกโป่ง
    stroke(80)
    strokeWeight(1)
    line(x, y + size_val * 0.6 + 8, x, y + size_val * 0.6 + 60)
    noStroke()


def draw():
    background(255)

    for i in range(num_balloons):
        # วาดลูกโป่งแต่ละลูกด้วยฟังก์ชัน draw_balloon
        draw_balloon(x_pos[i], y_pos[i], sizes[i],
                     colors[i][0], colors[i][1], colors[i][2])

        # Animation: ลอยขึ้นเรื่อยๆ
        y_pos[i] -= speeds[i]

        # ถ้าลอยพ้นจอด้านบน ให้กลับไปเริ่มที่ด้านล่างใหม่
        if y_pos[i] < -100:
            y_pos[i] = height + 50
