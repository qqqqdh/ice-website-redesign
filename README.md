# 정보통신공학과 홈페이지

성결대학교 정보통신공학과 웹프로그래밍 팀 프로젝트 시안입니다. HTML·CSS·JavaScript로 구성한 정적 웹사이트입니다.

## 실행

`index.html`을 브라우저에서 바로 엽니다. Node.js, 패키지 설치, 빌드가 필요하지 않습니다. 정적 웹 호스팅에도 그대로 올릴 수 있습니다.

## 파일 구성

- `index.html`: 메뉴, 공지사항, 학사일정, 학과소개, 학과활동과 상세창의 HTML. 콘텐츠도 이 파일에서 수정합니다.
- `src/style.css`: 색상, 버튼, 탭, 상세창과 PC·모바일 반응형 배치.
- `src/app.js`: 모바일 메뉴, 공지 탭 전환, 상세창 열기·닫기와 키보드 조작.
- `assets/`: 메인 이미지, 교표와 하단 슬로건.
- `licenses/`: 외부 디자인 자산과 관련 라이선스 고지.

## 디자인 참고

팀 디자인 자산: https://astryx-design-gallery.selbo06.chatgpt.site

## 동작

공지 유형은 마우스 또는 좌우 방향키·Home·End로 선택합니다. 공지나 학과활동을 누르면 기본 HTML `dialog` 상세창이 열리며 닫기 버튼, Escape 또는 배경 클릭으로 닫습니다. 모바일 메뉴는 메뉴 버튼이나 Escape로 닫을 수 있습니다.

공지·학사일정·학과활동은 예시 데이터입니다. 최신 브라우저의 기본 dialog 기능을 사용합니다.

## 수정 반영

HTML, CSS 또는 JavaScript를 수정하고 브라우저를 새로고침합니다.

## GitHub Pages 배포

예정 배포 주소: https://qqqqdh.github.io/ice-website-redesign/

최초 한 번 저장소 Settings → Pages → Build and deployment → Source에서 **GitHub Actions**를 선택합니다. 이후 Actions → Deploy to GitHub Pages → Run workflow로 첫 배포를 실행합니다.

그다음부터는 `main` 브랜치에 변경 사항을 push하면 자동으로 배포됩니다. 실행 결과와 배포 링크는 Actions 및 `github-pages` 환경에서 확인할 수 있습니다.

워크플로는 `index.html`, `src/style.css`, `src/app.js`, `assets/`만 배포합니다. 링크와 파일 경로가 상대 경로이므로 저장소 하위 주소에서도 동작합니다.
