# 1월 11~12일 강의 필기
## Markdown (확장자.md)
> 일반 텍스트 기반의 경량 Markup 언어  
주로 개발자들이 텍스트와 코드를 작성해 문서화하기 위해 사용  

- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [문법 정리](https://gist.github.com/ihoneymon/652be052a0727ad59601)
- [테이블(표) 만들어주는 사이트](https://www.tablesgenerator.com/markdown_tables)

## CLI
> Command Line Interface  
명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식

### CLI를 왜 사용해야 할까?
- Graphic User Interface (GUI) 보다 성능을 더 적게 소모
- 수많은 서버와 개발 시스템이 CLI를 통한 조작 환경을 제공함

### CLI에서 .의 역할
- . = 현재 디렉토리, 현재 폴더
- .. = 상위 디렉토리, 부모 폴더

#### 디렉토리
- 절대경로 : Root 디렉토리부터 목적 지점까지의 모든 경로
  - 예시 : C:/Users/ssafy/Desktop
- 상대경로 : 현재 디렉토리부터 목적 지점까지의 경로
  - 예시 : 현재 C:/Users 일 때, 바탕화면으로의 상대경로는 ssafy/Desktop

## Git
> Global Information Tracker  
분산 버전 관리 시스템

[Git Guide](https://git-scm.com/book/ko/v2)

### 분삭식의 장점
- 중앙 서버에 의존하지 않음
  - 중앙 서버의 장애나 손실에 대비 용이
- 동시에 다양한 작업 수행
  - 개발자 간의 작업 충돌을 줄여주고 개발 생산성을 향상
- 하지만 보안 강도가 높은 정보는 여전히 중앙 집중식을 고수함

### Git의 역할
- 코드의 버전과 히스토리 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경사항 비교

즉, 코드 변경 이력을 기록하고 협업을 용이하게 함

### Git의 구조
- Working Directory : 실제 작업 중인 파일들이 위치하는 영역
- Staging Area : Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역
  - 모든 버전과 변경 이력이 기록됨
  - 버전을 저장하는 행위 = Commit을 찍다 (Snapshot 이라고도 함)
## Remote Repository (Github)
> 원격 저장소

- Gitlab, Github(무료), Bitbucket 등은 모두 원격 저장소 서비스를 제공하는 회사들

### Github에서 Repository 생성
Public - 모두에게 공개  
private - 허락된 사람에게만 공개  

생성 후 Setting → Conversation 에서 권한을 줘야 그 사람도 Push가 가능해짐

### 명령어
- mkdir 이름 : 폴더생성
- touch 이름.확장자 : 파일생성
- ls : 현재 폴더의 파일들 출력
  - -al : 숨겨진 것까지 모두 출력
- cd 경로 : 다른 폴더로 이동
- rm 파일명 : 파일 삭제
  - -r 폴더명 : 폴더 삭제
- git init : 로컬 저장소 설정
- git add 파일명 : 파일을 Staging Area로 올림
  - . 쓰면 모든 파일을 올림 
- git status : Staging Area의 상태를 보여주는 것 같음
- git commit -m '코멘트' : Staging Area의 모든 파일을 Repository에 기록
  - --ammend : 마지막 Commit의 메시지 수정
- git log : Commit한 이력을 모두 보여줌
- git remote -v : 원격 저장소가 있으면 보여줌
- git remote add (닉네임) 주소 : 원격저장소 등록 (기본 닉네임은 Origin)
- git remote rm 원격 저장소 이름 : 원격 저장소의 연결을 끊음
- git push -u 닉네임 현재브랜치 : '닉네임'의 마스터브랜치 내용을 업로드 (-u = upstream)
- git clone 주소 : 원격 저장소 전체를 복붙
  - 로컬 저장소가 없는 곳에 해야함
- git pull 주소 : 원격 저장소를 가져와 머지함
- rm -rf .git : git 저장소 삭제
- git config --global : git global 설정 보기
- code : 현재 폴더에서 VSCode를 실행
- :q = 탈출, :wq = 저장 후 탈출

### .gitignore 파일
- Staging Area에 올라가지 않게 예외처리
- 이미 Git의 관리를 받은 파일이나 폴더는 ignore가 적용되지 않음

[개발환경에 따라 Gitignore 목록을 만들어주는 사이트](https://www.toptal.com/developers/gitignore/)

### Github 활용법
- Til 저장소를 만들어 학습한 것들 기록
- 개인/팀 프로젝트 코드 공유
  - 개발 지원 시 평가 받는 용도로도 사용
- 오픈 소스 프로젝트 기여

### Github 기타
- README.md 파일로 Repository 대문 장식
- 내 닉네임인 Repository의 대문으로 Github 프로필 장식 가능
  - 다른 방법도 많음

> README.md 파일이란?  
프로젝트에 대한 설명, 사용방법, 문서화된 정보 등을 작성해 프로젝트에 대한 이해와 활용법을 제공한다.  
주로 프로젝트의 소개, 설치 및 설정 방법, 사용 예시, 라이선스 정보, 기여 방법 등을 포함한다.  
반드시 저장소 최상단에 위치해야 원격 저장소에서 올바르게 출력된다.
