import tkinter as tk
import random
import time

# =========================
# SMART ROOM ASSISTANT
# =========================

class SmartRoomAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Room Assistant")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e1e")

        self.running = True

        title = tk.Label(
            root,
            text="SMART ROOM ASSISTANT",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#1e1e1e"
        )
        title.pack(pady=10)

        self.frame = tk.Frame(root, bg="#2a2a2a")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # =========================
        # SENZORY
        # =========================

        self.temp_label = self.create_sensor_label("Teplota: -- °C")
        self.humidity_label = self.create_sensor_label("Vlhkosť: -- %")
        self.noise_label = self.create_sensor_label("Hluk: -- dB")
        self.light_label = self.create_sensor_label("Svetlo: -- %")
        self.motion_label = self.create_sensor_label("Pohyb: --")

        # =========================
        # STAVY
        # =========================

        self.system_title = tk.Label(
            self.frame,
            text="\nAKCIE SYSTÉMU",
            font=("Arial", 16, "bold"),
            fg="#00ffcc",
            bg="#2a2a2a"
        )
        self.system_title.pack()

        self.fan_status = self.create_status_label("Ventilátor: VYPNUTÝ")
        self.light_status = self.create_status_label("Svetlo: VYPNUTÉ")
        self.alarm_status = self.create_status_label("Alarm: VYPNUTÝ")

        # =========================
        # LOG
        # =========================

        log_title = tk.Label(
            self.frame,
            text="\nLOG SYSTÉMU",
            font=("Arial", 16, "bold"),
            fg="#ffaa00",
            bg="#2a2a2a"
        )
        log_title.pack()

        self.log_box = tk.Text(
            self.frame,
            height=8,
            bg="#111111",
            fg="white",
            font=("Consolas", 10)
        )
        self.log_box.pack(fill="x", padx=10, pady=10)

        self.update_sensors()

    # =========================
    # UI
    # =========================

    def create_sensor_label(self, text):
        label = tk.Label(
            self.frame,
            text=text,
            font=("Arial", 14),
            fg="white",
            bg="#2a2a2a"
        )
        label.pack(pady=5)
        return label

    def create_status_label(self, text):
        label = tk.Label(
            self.frame,
            text=text,
            font=("Arial", 13, "bold"),
            fg="#00ff00",
            bg="#2a2a2a"
        )
        label.pack(pady=3)
        return label

    # =========================
    # SENZORY
    # =========================

    def update_sensors(self):

        if self.running:

            temperature = random.randint(18, 35)
            humidity = random.randint(20, 90)
            noise = random.randint(20, 100)
            light = random.randint(0, 100)
            motion = random.choice([True, False])

            self.temp_label.config(
                text=f"Teplota: {temperature} °C"
            )

            self.humidity_label.config(
                text=f"Vlhkosť: {humidity} %"
            )

            self.noise_label.config(
                text=f"Hluk: {noise} dB"
            )

            self.light_label.config(
                text=f"Svetlo: {light} %"
            )

            self.motion_label.config(
                text=f"Pohyb: {'DETEKOVANÝ' if motion else 'ŽIADNY'}"
            )

            # =========================
            # TERMOSTAT
            # =========================

            if temperature > 28:
                self.fan_status.config(
                    text="Ventilátor: ZAPNUTÝ",
                    fg="#00ff00"
                )
                self.add_log("Teplota vysoká -> ventilátor zapnutý")

            else:
                self.fan_status.config(
                    text="Ventilátor: VYPNUTÝ",
                    fg="white"
                )

            # =========================
            # HLUK
            # =========================

            if noise > 75:
                self.alarm_status.config(
                    text="Alarm: AKTÍVNY",
                    fg="red"
                )
                self.add_log("Príliš hlučné prostredie!")

            else:
                self.alarm_status.config(
                    text="Alarm: VYPNUTÝ",
                    fg="white"
                )

            # =========================
            # SVETLO
            # =========================

            if light < 30:
                self.light_status.config(
                    text="Svetlo: ZAPNUTÉ",
                    fg="yellow"
                )
                self.add_log("Tma v miestnosti -> svetlo zapnuté")

            else:
                self.light_status.config(
                    text="Svetlo: VYPNUTÉ",
                    fg="white"
                )

            # =========================
            # POHYB
            # =========================

            if motion:
                self.add_log("Detekovaný pohyb")

        self.root.after(2000, self.update_sensors)

    # =========================
    # LOG
    # =========================

    def add_log(self, message):

        current_time = time.strftime("%H:%M:%S")

        self.log_box.insert(
            tk.END,
            f"[{current_time}] {message}\n"
        )

        self.log_box.see(tk.END)

# =========================
# SPUSTENIE
# =========================

root = tk.Tk()
app = SmartRoomAssistant(root)
root.mainloop()
