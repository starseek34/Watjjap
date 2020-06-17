# SSAFY 1학기 최종 PJT

## 1.팀원 정보 및 업무 분담 내역

### 팀원 정보

SSAFY 1학기 최종 프로젝트에서 우리 조는 우리 반에서 유일하게 3인 1조를 구성하게 되었다. 팀은 김상현(조장), 최환석(조원), 배상은(조원)으로 구성되었으며 2020년 06월 11일 조 편성이 끝나자 회의를 통해 이번 프로젝트에서 이루고자 하는 목표와 각자가 맡아 구현할 부분을 정하게 되었다.

### 업무 분담 내역

#### 김상현

**김상현** 조장은 백엔드 부분을 맡아서, 1.Django의 url들을 구성하였으며(`urls.py`), 2.Django에서 저장될 데이터들의 모델링(`models.py`)을 하였고 3.Serializer들을 통해 Json응답을 return하기 위한 로직(`views.py`)을 구성하였다. 백엔드 부분에서의 작업이 끝난 후에는, 4.프론트엔드의 `account`관련 기능(로그인, 로그아웃, 회원가입, 개인정보 수정 및 마이페이지 조회 등)을 구현하였다

#### 최환석

**최환석** 조원은 프론트엔드 부분을 맡아 1.`Vue`의 기본적인 구조들(`view`와 `component`)을 구성하였으며, 2.영화 검색 결과창 3.영화 상세 조회 페이지의 구성과 4.웹 사이트 전반적인 CSS 배치를 구현하였다. 또한 5.발표를 맡아 발표에 사용될 영상을 제작하고 녹음을 하였으며 6.프로젝트 초기 우리의 목표를 나타낸 목업을 카카오 오븐을 통해 만들었다.

#### 배상은

**배상은** 조원은 백엔드와 프론트엔드 부분의 데이터 통신을 맡아 1.Django에서 NaverAPI를 사용해 받아온 결과를 Vue로 리턴해주는 검색 페이지와 장르별 추천페이지를 구현하였으며 2.영화 상세 조회 페이지에 정보를 리턴하는 로직, 3.`Vue`에서 일어나는 도메인 처리와 리뷰 정보 조회 페이지 구성등을 하였다. 또한 4.업무에 필요한 잡무(프로젝트 일지 작성, README작성, Trello관리 등)를 맡아 처리하였다.

## 2.목표 서비스 구현 및 실제 구현 정도

### 목표 서비스

우리 조는 첫 회의당시에, 어떤 서비스를 구현하고자 하는가 결정에 많은 시간을 쏟았고, 긴 시간의 토론 끝에 국내에서 가장 유명한 영화 커뮤니티인 `WATCHA`를 벤치마크하여 `WATCHA`와 유사한 서비스를 하는 웹 프로젝트를 구현하는것에 모두 동의하였다. 이에 `KaKaoOven`을 통해 우리가 만들게 될 서비스를 미리 구상해보았고, `Trello`를 통해 어떤 기능들을 구현할 것인지 정리해보았다.

### 목표 서비스의 주요 내용

우리 조가 목표한 서비스의 주요 기능은 다음과 같다

1. 회원가입, 로그인, 로그아웃 기능과 회원 프로필(닉네임, 상태메세지)수정 기능
2. 네이버 영화 검색 API를 활용해 영화 검색시 영화 관련 정보 송출 기능
3. 사용자의 별점기능과 유저평점을 기반으로 유사한 영화 추천 및 랜덤 추천 기능
4. 영화 상세 정보 조회시 배우, 감독, 줄거리, 예고편, 동일 장르 영화 확인 기능
5. 영화 관련 리뷰를 남길수 있으며, 리뷰에 좋아요와 댓글이 달리는 커뮤니티 기능

### 실제 구현 정도

#### 완료

1. 회원가입, 로그인, 로그아웃 기능 구현 기능
2. 네이버 영화 검색 API를 활용한 영화 검색 기능
3. 랜덤 영화 추천 기능 및 유사 장르 영화 추천 기능
4. 영화 상서 정보 조회시 배우, 감독, 줄거리, 예고편, 동일 장르 영화 확인 기능(크롤링 사용)
5. 영화 리뷰 생성 및 영화 리뷰 확인 기능

#### 미완

1. 회원 프로필 수정 기능
2. 사용자의 별점/좋아요 기능과 평점 기반으로 한 추천 기능
3. 영화 상세 정보 조회 시 감독, 배우들의 얼굴이 나오는 기능
4. 영화 리뷰에 대한 좋아요와 댓글 생성 기능 및 영화 리뷰 삭제 기능

## 3.데이터베이스 모델링(ERD)

총 4개의 모델(Movie, User, Review, Comment)을 가지며 Movie는 User와 좋아요 혹은 별점 기능을 통해 M:N의 관계를 가지며, Movie와 Review는 review 생성을 통해 1:N관계를 가진다. 또한 User와 Review는 review 생성을 통해 1:N관계를 가지며, User와 Comment는 comment 생성을 통해 1:N, Review와 Comment 또한 comment 생성을 통해 1:N 관계를 가지게 된다

이 밖에 각 모델들의 속성(attribute)과 key값들은 첨부한 ER다이어그램을 통해 확인할 수 있다.

## 4.필수 기능

### 명세서에서 제시한 구현 / 서비스 필수 기능

1. 관리자 권한의 유저만 영화 등록 / 수정 / 삭제 기능
2. 관리자 권한의 유저만, 다른 일반 유저를 관리하는 기능
3. DB에 최소 50개 이상의 데이터 삽입
4. 로그인 된 유저에 한해 평점 등록 / 수정 / 삭제 기능
5. 유저 정보 기반 영화 추천 기능
6. 커뮤니티 관련 로그인 유저 대상 리뷰, 댓글 작성 / 수정 / 삭제 기능
7. 최소 5개 이상의 URL및 페이지 생성

#### 실제 구현

1. DB에 50개 이상의 데이터 삽입 ==> 영화 상세 정보 조회 시 바로 DB에 영화 데이터가 저장되는 방식이기에 50개 이상의 데이터들이 존재할 수 있음
2. 로그인 유저에 대해 영화 추천(랜덤 및 장르별)기능 구현 완료
3. 커뮤니티에서 리뷰 작성 기능 구현
4. 최소 5개 이상의 URL구현(Home, MyPage, Recommend, Search, Detail, ReviewDetail 등)완료

#### 미구현

1. 관리자 권한 기능(영화 등록 / 수정 / 삭제 및 유저 관리)
2. 유저 정보 기반 영화 추천 기능
3. 영화에 대해 평점 등록 / 수정 / 삭제 기능
4. 커뮤니티의 리뷰 수정 / 삭제 및 댓글 등록 / 수정 / 삭제

## 5.배포 서버 URL

Heroku를 통해 배포(2020.06.17.예정)시 업로드 예정

## 6.기타(느낀점)

### 1.업무 분담 방식의 중요성

이번 프로젝트는 SSAFY 교육 과정 중 1학기의 대미를 장식하는 프로젝트였으며, 교육생들이 최초로 접하는 장기 프로젝트였기에 나에게 조금 특별하게 다가왔다. 심지어 우리 조는 행운까지 따라서 좋은 사람들과 함께하는, 반 내 유일한 3인 1조였기에 프로젝트 시작때만 하여도 조원 모두는 프로젝트에 대해 낙관하였다. 프로젝트 첫날 우리는 WATCHA라는 목표를 설정하였다. 조원 마다 각자가 자신있어 하는 부분이 달랐고, 또 구현해보고 싶어 하는 부분이 달랐기에 원하는 것에 따라 작업을 배분하여 프로젝트를 진행하였다. 하지만 결국 이번 웹 프로젝트는 하나의 거대한 유기체와 같이 얽혀있었기에 나눈다고 하여도 완벽하게 나눌 수 없었고 여기에서 조금 시행착오가 발생하게 되었다. 우리의 처음의 목표는 백엔드와 프런트엔드 그리고 API활용을 완벽하게 분할하여 작업하고자 하였으나, 이것은 너무 이상에 가까웠다. 기능 하나를 구현하기 위해서는 결국 프런트와 백을 오가며 데이터들을 주고받아야했기에, 한 분야에만 치우쳐서 기능을 구현하는것은 너무나도 어렵게 다가왔고 여기에서 시간을 많이 소비하게 되었다. 이로 인해 필수 기능이나 목표한 기능 중 몇몇개를 구현하지 못하였고 마감 시간의 압박에 쫓기어서 아쉬운 프로젝트가 되었다. 다음 번 프로젝트시에는 반드시 각각 날짜별로 무슨 기능을 구현할 것인지 명확히 정리하고, 프론트엔드와 백엔드를 칼같이 나누기보다는 기능별로 사람마다 맡아 나누어 구현하는 방식을 채택해야겠다고 생각하게 되었다.

### 2.Vue

이번 프로젝트를 통해 가장 많이 향상된 능력을 꼽으라면 아마 Vue를 다루는 방법일 것이다. Vue를 사용하며 라우터를 어떻게 사용하는지, 라우터 푸쉬를 하면서 Variable routing 이외에도 어떻게 인자를 넘기는지, 쿠키를 어떻게 Vue에서 다룰수 있는 지 등을 잘 알게 되었던 프로젝트였다.

### 3.CSS와 Bootstrap

이번 프로젝트에서 우리를 가장 많이 괴롭힌것은 `CSS`와 `Bootstrap`이다. SSAFY 1학기 강의 중에 교수님이 하신 **'커튼을 올리고, 내린다'**를 이번 프로젝트를 통해 완벽하게 이해했으며, 1mm의 간격을 수정하기 위해 수많은 커튼을 올리고 내리기를 반복하였다. 그리고 다시금 CSS와 Bootstrap을 복습해야겠다고 깨닫게 되었다.

### 4.프로젝트를 마무리하며

프로젝트를 마무리하니 벌써 SSAFY에서의 반년이 끝났다는 것을 새삼 느끼게 되었다. 설렘으로 가득찬 1월부터 시작해서, 코로나로 인한 인터넷강의와 이번 최종프로젝트 까지 쉴새없는 6개월이었다. 

조원들의 구성부터 시작해서 서비스를 개발하고 배포하는 것 까지 이번 프로젝트의 모든 내용은 SSAFY의 1학기를 함축시켜놓은 것이었기에, 1학기의 최종 프로젝트라는 이름에 걸맞았다. 정말로 즐겁게 진행하였고, 조금이라도 더 좋은 결과물을 만들기 위해 많은 노력을 하였다. 비록 몇몇 기능 구현과 완성에는 실패하여 아쉬움이 남지만, 그래도 유의미하고 뜻깊은 결과물을 만들어낼 수 있었던 것은 모두 같이 협력하고 도와준 조원(김상현, 최환석)들의 노력과 교수님(유태영 교수님, 정종윤 교수님)의 훌륭한 가르침 덕분이므로 모두에게 감사의 마음을 전하며 프로젝트를 마무리한다.

최종 프로젝트, 그리고 SSAFY 1학기 교육 끝!