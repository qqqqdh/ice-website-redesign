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

배포 주소: https://qqqqdh.github.io/ice-website-redesign/

최초 한 번 저장소 Settings → Pages → Build and deployment → Source에서 **GitHub Actions**를 선택합니다. 이후 Actions → Deploy to GitHub Pages → Run workflow로 첫 배포를 실행합니다.

그다음부터는 PR이 `main` 브랜치에 병합되면 자동으로 배포됩니다. 실행 결과와 배포 링크는 Actions 및 `github-pages` 환경에서 확인할 수 있습니다.

워크플로는 `index.html`, `src/style.css`, `src/app.js`, `assets/`만 배포합니다. 링크와 파일 경로가 상대 경로이므로 저장소 하위 주소에서도 동작합니다.

## GitHub Flow로 작업하기

1. 최신 `main`에서 작업별 브랜치를 만듭니다. 예: `feature/notice-list`, `fix/mobile-menu`.
2. 수정 내용을 커밋하고 작업 브랜치에 push합니다.
3. `main`을 대상으로 PR을 열고 변경 이유와 확인 결과를 적습니다.
4. `Site checks` 통과와 팀원 1명 이상의 승인을 받은 뒤 병합합니다. 수정 커밋을 추가하면 다시 검사하고 승인을 받습니다.
5. Pages 배포 성공을 확인하고 병합한 작업 브랜치를 삭제합니다.

`main` 보호 규칙은 GitHub 저장소 설정에서 관리합니다. 관리자에게도 PR·승인·필수 검사를 적용하며, 강제 push와 브랜치 삭제를 허용하지 않습니다.

PR 자동 검사는 JavaScript 문법, HTML 태그 중첩, 중복 ID, HTML에서 참조한 로컬 파일, 내부 링크와 접근성 ID 연결을 확인합니다. 화면 배치와 실제 브라우저 조작은 PR 작성자가 별도로 확인합니다.

같은 검사를 로컬에서 실행하려면 Node.js와 Python 3.10 이상이 필요합니다. 사이트를 여는 데에는 설치가 필요하지 않습니다.

```sh
node --check src/app.js
python -B -m unittest discover -s tests
python -B scripts/check_site.py
```
