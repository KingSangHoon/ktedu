# 라마 모델 기반 코드 정적 분석 도구

## 프로젝트 개요
Git 커밋 이력을 활용하여 라마(Llama) 모델로 코드 정적 분석을 수행하는 도구입니다.

## 핵심 기능
- Git 저장소 커밋 이력 분석
- 라마 모델을 통한 코드 품질 평가
- 코드 스타일 및 패턴 분석
- 잠재적 버그 및 개선사항 제안

## 시스템 구조

### 입력
- **Git 저장소 정보**: Repository URL, Branch 정보
- **커밋 정보**: 특정 커밋 범위, 파일 경로
- **분석 옵션**: 분석 깊이, 대상 언어

### 처리 과정
1. Git API를 통한 커밋 데이터 수집
2. 변경된 코드 추출 및 전처리
3. 라마 모델에 코드 분석 요청
4. 분석 결과 후처리 및 리포트 생성

### 출력
- 코드 품질 점수
- 개선 권장사항
- 보안 취약점 분석
- 성능 최적화 제안

## 기술 스택

### Backend
- **언어**: Java 17+
- **프레임워크**: Spring Boot 3.x
- **Git 연동**: JGit Library
- **AI 모델**: Llama 2/3 (Ollama 또는 API)

### Frontend
- **UI 프레임워크**: React 또는 Thymeleaf
- **차트**: Chart.js (분석 결과 시각화)

### Database
- **분석 결과 저장**: PostgreSQL
- **캐싱**: Redis

## 설치 및 실행

### 사전 요구사항
```bash
- Java 17+
- Maven 3.8+
- Git 2.30+
- Ollama (라마 모델 실행환경)
```

### 로컬 실행
```bash
# 저장소 클론
git clone https://github.com/username/llama-code-analysis.git
cd llama-code-analysis

# 의존성 설치
mvn clean install

# 애플리케이션 실행
mvn spring-boot:run
```

### Docker 실행
```bash
docker-compose up -d
```

## 사용법

### 1. Git 저장소 등록
```
Repository URL: https://github.com/username/project.git
Branch: main
Commit Range: HEAD~10..HEAD
```

### 2. 분석 옵션 설정
```
- 분석 언어: Java, Python, JavaScript
- 분석 깊이: 표면적 / 심화 분석
- 포함할 파일 패턴: *.java, *.py
```

### 3. 결과 확인
- 대시보드에서 분석 결과 확인
- PDF/HTML 리포트 다운로드
- API를 통한 결과 조회

## API 명세

### 분석 요청
```http
POST /api/analyze
Content-Type: application/json

{
  "repositoryUrl": "https://github.com/username/repo.git",
  "branch": "main",
  "commitRange": "HEAD~5..HEAD",
  "language": "java",
  "analysisDepth": "deep"
}
```

### 결과 조회
```http
GET /api/analysis/{analysisId}
```

## 설정

### application.yml
```yaml
llama:
  model: llama2:7b
  endpoint: http://localhost:11434
  timeout: 30s

git:
  clone-timeout: 60s
  max-file-size: 1MB

analysis:
  max-commits: 100
  supported-languages: [java, python, javascript]
```

## 라마 모델 프롬프트 예시
```
다음 Java 코드의 품질을 분석하고 개선사항을 제안해주세요:

[코드 내용]

분석 항목:
1. 코드 스타일 준수
2. 성능 최적화 가능성
3. 보안 취약점
4. 유지보수성
5. 테스트 가능성
```

## 프로젝트 구조
```
src/
├── main/java/
│   ├── controller/     # REST API 컨트롤러
│   ├── service/        # 비즈니스 로직
│   ├── model/          # 데이터 모델
│   ├── config/         # 설정 클래스
│   └── util/           # 유틸리티
├── main/resources/
│   ├── templates/      # Thymeleaf 템플릿
│   └── static/         # 정적 파일
└── test/               # 테스트 코드
```

## 향후 계획
- [ ] 다중 언어 지원 확대
- [ ] 실시간 분석 기능
- [ ] GitHub Actions 연동
- [ ] 팀 협업 기능
- [ ] 머신러닝 기반 패턴 학습

## 라이센스
MIT License

## 기여 방법
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request
