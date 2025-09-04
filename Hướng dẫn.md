# 🚀 Hướng dẫn Upload lên GitHub và Auto Build

## 📋 Chuẩn bị

### 1. Tạo cấu trúc thư mục
```
2048-game/
├── main.py                 # Game chính (Pygame)
├── kivy_main.py            # Phiên bản mobile (Kivy)
├── requirements.txt        # Dependencies
├── setup.py               # Package setup
├── pyproject.toml         # Modern Python project config
├── buildozer.spec         # Android build config
├── Dockerfile             # Docker config
├── docker-compose.yml     # Docker compose
├── Makefile              # Build commands
├── README.md             # Documentation
├── .github/
│   └── workflows/
│       └── build.yml      # GitHub Actions
└── .gitignore            # Git ignore file
```

### 2. Tạo file .gitignore
```bash
# Tạo file .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Game saves
best_score.json
saves/

# Build artifacts
*.spec
bin/
.buildozer/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
EOF
```

## 🔧 Thiết lập GitHub Repository

### Bước 1: Tạo Repository trên GitHub
1. Đăng nhập GitHub.com
2. Click "New repository"
3. Đặt tên: `2048-game`
4. Chọn "Public" (để GitHub Actions miễn phí)
5. Không tích "Initialize with README" (vì ta đã có sẵn)
6. Click "Create repository"

### Bước 2: Upload code lên GitHub

```bash
# Di chuyển vào thư mục project
cd 2048-game

# Khởi tạo git repository
git init

# Thêm tất cả files
git add .

# Commit đầu tiên
git commit -m "Initial commit: 2048 game with multi-platform support"

# Thêm remote origin (thay YOUR_USERNAME bằng tên GitHub của bạn)
git remote add origin https://github.com/YOUR_USERNAME/2048-game.git

# Đổi branch main
git branch -M main

# Push code lên GitHub
git push -u origin main
```

## 🤖 Thiết lập GitHub Actions

### GitHub Actions sẽ tự động chạy khi:
- Push code lên branch `main` hoặc `develop`
- Tạo Pull Request
- Tạo tag với format `v*` (ví dụ: v1.0.0)

### Các job sẽ chạy:
1. **build-windows**: Tạo file .exe cho Windows
2. **build-macos**: Tạo executable cho macOS  
3. **build-linux**: Tạo executable cho Linux
4. **build-android**: Tạo file .apk cho Android
5. **release**: Tự động tạo release khi có tag

## 🎯 Cách trigger build

### 1. Build thông thường (Push code)
```bash
# Sửa code và commit
git add .
git commit -m "Add new feature"
git push origin main
```

### 2. Build và tạo release
```bash
# Tạo tag version
git tag v1.0.0
git push origin v1.0.0
```

## 📱 Build từng platform riêng lẻ

### Windows (Local build)
```bash
# Cài đặt PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name "2048-Game" main.py

# File sẽ ở trong thư mục dist/
```

### Android (Local build)
```bash
# Cài đặt Buildozer
pip install buildozer

# Khởi tạo buildozer (chỉ lần đầu)
buildozer init

# Build APK debug
buildozer android debug

# Build APK release (cần signing key)
buildozer android release
```

### Docker build
```bash
# Build Docker image
docker build -t 2048-game .

# Chạy với docker-compose
docker-compose up -d
```

## 🔍 Theo dõi build process

### 1. Xem GitHub Actions
- Vào repository GitHub
- Click tab "Actions"
- Xem các workflow đang chạy

### 2. Download artifacts
- Sau khi build xong, vào tab "Actions"
- Click vào workflow run
- Scroll xuống phần "Artifacts"
- Download file cần thiết

### 3. Releases
- Khi push tag, GitHub sẽ tự tạo release
- Vào tab "Releases" để download

## 🛠️ Troubleshooting

### Lỗi thường gặp:

#### 1. Build Android lỗi
```yaml
# Thêm vào build.yml nếu lỗi NDK
- name: Setup Android NDK
  run: |
    echo "y" | $ANDROID_HOME/tools/bin/sdkmanager "ndk;21.4.7075529"
```

#### 2. PyInstaller lỗi missing modules
```bash
# Thêm hidden imports
pyinstaller --onefile --windowed --hidden-import=pygame --name "2048-Game" main.py
```

#### 3. Kivy build lỗi dependencies
```bash
# Cài thêm dependencies
sudo apt-get install python3-dev libffi-dev
```

## 📊 Monitoring và Logs

### Xem build logs:
1. Vào GitHub Actions
2. Click vào workflow run
3. Click vào job muốn xem
4. Xem detailed logs

### Status badges (Thêm vào README):
```markdown
![Build Status](https://github.com/YOUR_USERNAME/2048-game/workflows/Build%20Multi-Platform%202048%20Game/badge.svg)
```

## 🎉 Deploy options

### 1. GitHub Pages (cho web version)
- Tạo branch `gh-pages`
- Upload HTML version
- Enable GitHub Pages

### 2. Microsoft Store (Windows)
- Dùng file .exe từ GitHub Actions
- Submit lên Microsoft Store

### 3. Google Play Store (Android)
- Build signed APK
- Upload lên Play Console

### 4. Mac App Store (macOS)
- Cần Apple Developer account
- Code signing và notarization

## 🔄 Workflow tự động

### Khi bạn:
1. **Push code** → Auto build tất cả platforms
2. **Create PR** → Build và test
3. **Merge PR** → Deploy to staging
4. **Create tag** → Build và release
5. **Release** → Notify users

### Example workflow:
```bash
# Develop new feature
git checkout -b feature/new-feature
# ... code changes ...
git commit -m "Add new feature"
git push origin feature/new-feature

# Create PR on GitHub
# After review and merge:

# Create release
git checkout main
git pull origin main
git tag v1.1.0
git push origin v1.1.0
```

## 🎯 Tips và Best practices

1. **Versioning**: Dùng semantic versioning (v1.0.0)
2. **Testing**: Thêm tests trước khi build
3. **Security**: Không commit API keys
4. **Documentation**: Cập nhật README.md
5. **Changelog**: Ghi lại thay đổi mỗi version

Với setup này, bạn sẽ có một pipeline CI/CD hoàn chỉnh cho game 2048! 🚀
