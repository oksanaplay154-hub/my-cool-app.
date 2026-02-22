from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CameraApp(App):
    def build(self):
        # Создаем вертикальное расположение элементов
        layout = BoxLayout(orientation='vertical')
        
        # Создаем объект камеры (индекс -1 или 0 обычно основная камера)
        self.camera = Camera(play=True, resolution=(640, 480))
        
        # Кнопка для красоты (можно добавить функционал снимка)
        btn = Button(text="Camera is Running", size_hint_y=0.1)
        
        layout.add_widget(self.camera)
        layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    CameraApp().run()
