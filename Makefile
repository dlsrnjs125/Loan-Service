# Loan Service Makefile
# 간편한 개발 환경 관리를 위한 명령어 모음

.PHONY: help install local migrate clean shell check format format-check

# 기본 타겟
.DEFAULT_GOAL := help

help: ## 도움말 표시
	@echo "Loan Service - 개발 명령어"
	@echo ""
	@echo "사용법:"
	@echo "  make [명령어]"
	@echo ""
	@echo "주요 명령어:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ============================================================================
# 설치 및 설정
# ============================================================================

install: ## 의존성 설치
	@echo "📦 Installing dependencies..."
	@if [ ! -d "venv" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv venv; \
	fi
	@echo "Installing packages..."
	@source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

# ============================================================================
# 개발 서버 실행
# ============================================================================

local: ## 개발 서버 실행 (포그라운드)
	@echo "🚀 Starting development server..."
	@if [ ! -d "venv" ]; then \
		echo "❌ Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	@if [ "$(filter bg,$(MAKECMDGOALS))" ]; then \
		echo "Starting server in background..."; \
		. venv/bin/activate && nohup python manage.py runserver > /tmp/loan-service.log 2>&1 & \
		echo "$$!" > /tmp/loan-service.pid; \
		sleep 2; \
		if ps -p $$(cat /tmp/loan-service.pid) > /dev/null 2>&1; then \
			echo "✅ Server started in background (PID: $$(cat /tmp/loan-service.pid))"; \
			echo "Access at: http://localhost:8000"; \
			echo "Logs: tail -f /tmp/loan-service.log"; \
		else \
			echo "❌ Failed to start server. Check logs: cat /tmp/loan-service.log"; \
			exit 1; \
		fi; \
	else \
		. venv/bin/activate && python manage.py runserver; \
	fi

# ============================================================================
# 데이터베이스 관리
# ============================================================================

migrate: ## 데이터베이스 마이그레이션 실행
	@echo "🔄 Running migrations..."
	@source venv/bin/activate && python manage.py migrate
	@echo "✅ Migrations complete!"

makemigrations: ## 마이그레이션 파일 생성
	@echo "📝 Creating migration files..."
	@source venv/bin/activate && python manage.py makemigrations
	@echo "✅ Migration files created!"

# ============================================================================
# 코드 포맷팅 및 품질
# ============================================================================

format: ## 코드 포맷팅 및 린팅 (ruff)
	@echo "🔥 Formatting code with ruff..."
	@if [ ! -d "venv" ]; then \
		echo "❌ Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	@. venv/bin/activate && ruff format .
	@. venv/bin/activate && ruff check . --fix
	@echo "✅ Code formatting & checking complete!"

format-check: ## 코드 포맷팅 체크만 (수정 안함)
	@echo "🔍 Checking code format with ruff..."
	@if [ ! -d "venv" ]; then \
		echo "❌ Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	@. venv/bin/activate && ruff format --check .
	@. venv/bin/activate && ruff check .
	@echo "✅ Code format check complete!"

# ============================================================================
# 유틸리티
# ============================================================================

check: ## Django 시스템 체크
	@echo "🔍 Running system check..."
	@source venv/bin/activate && python manage.py check
	@echo "✅ System check complete!"

shell: ## Django shell 실행
	@echo "🐚 Starting Django shell..."
	@source venv/bin/activate && python manage.py shell

createsuperuser: ## 슈퍼유저 생성
	@echo "👤 Creating superuser..."
	@source venv/bin/activate && python manage.py createsuperuser

collectstatic: ## 정적 파일 수집
	@echo "📦 Collecting static files..."
	@source venv/bin/activate && python manage.py collectstatic --noinput
	@echo "✅ Static files collected!"

# ============================================================================
# 정리 및 종료
# ============================================================================

clean: ## 서버 종료 및 포트 정리
	@echo "🛑 Stopping development server..."
	@lsof -ti:8000 | xargs kill -9 2>/dev/null || echo "No server running on port 8000"
	@echo "🧹 Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete!"

stop: ## 서버만 종료
	@echo "🛑 Stopping server..."
	@if [ -f /tmp/loan-service.pid ]; then \
		kill $$(cat /tmp/loan-service.pid) 2>/dev/null || true; \
		rm -f /tmp/loan-service.pid; \
		echo "✅ Server stopped (from PID file)"; \
	fi
	@lsof -ti:8000 | xargs kill -9 2>/dev/null || echo "No server running on port 8000"
	@echo "✅ Server stopped!"

# ============================================================================
# 테스트
# ============================================================================

test: ## 테스트 실행
	@echo "🧪 Running tests..."
	@source venv/bin/activate && python manage.py test
	@echo "✅ Tests complete!"

# ============================================================================
# 더미 타겟 (인자로 사용되는 명령어들)
# ============================================================================

.PHONY: bg
bg:
	@:

