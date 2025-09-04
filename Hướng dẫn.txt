# ⚡ Quick Start - 2048 Game

## 🚀 Phương pháp 1: Tự động (Khuyến nghị)

### Bước 1: Chạy setup script
```bash
# Download và chạy setup script
curl -O https://raw.githubusercontent.com/your-repo/setup_project.sh
chmod +x setup_project.sh
./setup_project.sh
```

### Bước 2: Copy artifacts
1. Copy tất cả nội dung từ các artifacts Claude đã tạo
2. Paste vào các file tương ứng trong project

### Bước 3: Test và deploy
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Test game
python main.py

# Push to GitHub (nếu chưa tự động)
git push origin main

# Create release
git tag v1.0.0
git push origin v1.0.0
```

---

## 🛠️ Phương pháp 2: Thủ công

### Bước 1: Tạo GitHub Repository
1. Đăng nhập GitHub.com
2. Click "New repository"
3. Tên: `2048-game`
4. Chọn "Public"
5. Click "Create repository"

### Bước 2: Setup local project
```bash
# Tạo thư mục project
mkdir 2048-game
cd 2048-game

# Khởi tạo git
git init
```

### Bước 3: Tạo cấu trúc files
```bash
# Tạo cấu trúc thư mục
mkdir -p .github/workflows
mkdir -p tests

# Tạo .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
build/
dist/
*.egg-info/
venv/
.DS_Store
best_score.json
.buildozer/
bin/
EOF
```

### Bước 4: Copy artifacts
Copy từng file từ Claude artifacts:

1. **main.py** ← Game Pygame chính
2. **kivy_main.py** ← Game mobile version
3. **requirements.txt** ← Dependencies
4. **setup.py** ← Package setup
5. **pyproject.toml** ← Modern Python config
6. **buildozer.spec** ← Android build config
7. **.github/workflows/build.yml** ← GitHub Actions
8. **Dockerfile** ← Docker config
9. **docker-compose.yml** ← Docker Compose
10. **Makefile** ← Build automation
11. **README.md** ← Documentation

### Bước 5: Upload lên GitHub
```bash
# Add remote repository (thay YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/2048-game.git

# Add và commit files
git add .
git commit -m "Initial commit: 2048 game with multi-platform support"

# Push lên GitHub
git branch -M main
git push -u origin main
```

---

## 🎯 Trigger Builds

### Build thường (mỗi khi push)
```bash
git add .
git commit -m "Update game features"
git push origin main
```
→ Sẽ tự động build tất cả platforms

### Build và tạo Release
```bash
git tag v1.0.0
git push origin v1.0.0
```
→ Sẽ tự động tạo release với tất cả executables

## 📱 Kết quả Build

Sau khi build xong, bạn sẽ có:

### Artifacts (GitHub Actions):
- `2048-Game-Windows/2048-Game.exe` - Windows executable
- `2048-Game-macOS/2048-Game` - macOS executable  
- `2048-Game-Linux/2048-Game` - Linux executable
- `2048-Game-Android/game2048-1.0-debug.apk` - Android APK

### Release (khi tạo tag):
- Tự động tạo GitHub Release
- Attach tất cả executables
- Ready để distribute!

## 🔍 Monitor Builds

### Xem build progress:
1. Vào GitHub repository
2. Click tab "Actions"
3. Xem workflows đang chạy
4. Click vào run để xem chi tiết

### Download executables:
1. Sau khi build xong, vào "Actions"
2. Click vào workflow run thành công
3. Scroll xuống "Artifacts"
4. Download file cần thiết

## ⚡ One-liner Setup

Nếu bạn muốn setup nhanh nhất:

```bash
# Tạo project directory
mkdir 2048-game && cd 2048-game

# Khởi tạo git và cấu trúc cơ bản
git init && mkdir -p .github/workflows tests

# Tạo gitignore cơ bản
echo -e "__pycache__/\n*.pyc\nbuild/\ndist/\nvenv/\n.DS_Store\nbest_score.json" > .gitignore

# Sau đó copy tất cả artifacts vào và:
git add . && git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/2048-game.git
git branch -M main && git push -u origin main

# Tạo release đầu tiên
git tag v1.0.0 && git push origin v1.0.0
```

## 🎮 Test Local

Trước khi push lên GitHub, test local:

```bash
# Tạo virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc venv\Scripts\activate  # Windows

# Cài dependencies
pip install -r requirements.txt

# Test Pygame version
python main.py

# Test Kivy version  
python kivy_main.py

# Test build executable
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

Chúc bạn thành công! 🚀
