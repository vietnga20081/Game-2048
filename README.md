# Game-2048
# 🎮 Game 2048

Một phiên bản game 2048 được viết bằng Python với Pygame, hỗ trợ build đa nền tảng thông qua GitHub Actions.

## ✨ Tính năng

- 🎯 Game 2048 cổ điển với giao diện đẹp mắt
- 🏆 Lưu điểm cao nhất
- 🎮 Điều khiển bằng phím WASD hoặc mũi tên
- 🔄 Khởi động lại game bằng phím R
- 📱 Hỗ trợ đa nền tảng: Windows, macOS, Linux, Android
- 🏗️ Tự động build với GitHub Actions

## 🚀 Cài đặt và chạy

### Chạy từ source code

1. **Clone repository:**
```bash
git clone <your-repo-url>
cd 2048-game
```

2. **Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

3. **Chạy game:**
```bash
python main.py
```

### Chạy từ executable

Tải file executable từ [Releases](../../releases) tương ứng với hệ điều hành của bạn:
- Windows: `2048-Game.exe`
- macOS: `2048-Game`
- Linux: `2048-Game`
- Android: `game2048-1.0-debug.apk`

## 🎮 Cách chơi

- **Di chuyển:** Sử dụng phím WASD hoặc mũi tên
- **Mục tiêu:** Kết hợp các ô số để đạt được ô 2048
- **Khởi động lại:** Nhấn phím R
- **Thoát:** Nhấn ESC hoặc đóng cửa sổ

## 🏗️ Build và Deploy

### GitHub Actions Workflow

Repository này được cấu hình để tự động build cho tất cả các platform khi:
- Push code lên branch `main` hoặc `develop`
- Tạo pull request
- Tạo tag với format `v*` (ví dụ: v1.0.0)

### Các platform được hỗ trợ:

1. **Windows** - Sử dụng PyInstaller
2. **macOS** - Sử dụng PyInstaller
3. **Linux** - Sử dụng PyInstaller
4. **Android** - Sử dụng Buildozer và Kivy

### Tự build thủ công:

#### Windows/macOS/Linux:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "2048-Game" main.py
```

#### Android:
```bash
pip install buildozer
buildozer init
buildozer android debug
```

## 📁 Cấu trúc project

```
2048-game/
├── main.py                 # Game chính (Pygame)
├── kivy_main.py            # Phiên bản Kivy cho mobile
├── requirements.txt        # Python dependencies
├── setup.py               # Cấu hình package
├── buildozer.spec         # Cấu hình Buildozer cho Android
├── .github/
│   └── workflows/
│       └── build.yml      # GitHub Actions workflow
└── README.md              # Tài liệu này
```

## 🛠️ Phát triển

### Thêm tính năng mới:
1. Fork repository
2. Tạo branch mới: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Tạo Pull Request

### Chạy tests:
```bash
python -m pytest tests/
```

## 📦 Dependencies

### Core:
- `pygame>=2.5.2` - Game engine
- `kivy>=2.2.0` - Mobile UI framework
- `kivymd>=1.1.1` - Material Design components

### Build tools:
- `pyinstaller` - Tạo executable
- `buildozer` - Android build tool
- `cython` - Compilation optimization

## 🎯 Roadmap

- [ ] Thêm animations mượt mà hơn
- [ ] Hỗ trợ touch controls cho mobile
- [ ] Thêm sound effects
- [ ] Online leaderboard
- [ ] Dark mode
- [ ] Multiple grid sizes (3x3, 5x5, 6x6)
- [ ] Undo functionality
- [ ] Save/load game state

## 🤝 Đóng góp

Contributions, issues và feature requests đều được hoan nghênh!

## 📄 License

Dự án này được phân phối dưới MIT License. Xem `LICENSE` để biết thêm thông tin.

## 📞 Liên hệ

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

⭐ Nếu bạn thích project này, hãy cho nó một star nhé!
