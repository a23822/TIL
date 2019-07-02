# HTML meta Tag 정리



1. Meta tag 란?

   Metadata 를 제공하는 역할을 하는 태그입니다.
   화면에 별달리 표시되는 것이 없지만 검색 엔진이나 브라우저에 읽힙니다.
   Meta 태그는 보통 name 과 value 쌍으로 사용됩니다.

   ex)

   ``` html
   <!DOCTYPE html>
   <meta charset="UTF-8"> <!-- 인코딩 방식 -->
   <meta name="viewport" content="widrh=device-width, initial-scale=1.0"> <!-- 뷰포트 설정-->
   <meta name="채찬우" content="마크다운 정리"> <!-- 저작자 표시 -->
   ```

   meta tag 의 속성으로는 http-equiv, name, content  총 3가지 속성이 있습니다.

   - http-equiv = '항목명'
     웹 브라우저가 서버에 명령을 내리는 속성으로 name 속성을 대신하여 사용될 수 있으며, HTML 문서가 응답 헤더와 함께 웹 서버로부터 웹 브라우저에 전송되었을 때에만 의미를 갖습니다.
   - content = '정보값'
     meta 정보의 내용을 저장합니다.
   - name = '정보 이름'
     몇 개의 meta 정보의 이름을 정할 수 있으며 지정하지 않으면 http-equiv 와 같은 기능을 합니다.

2. Meta tag 의 종류

   ``` html
   <meta name='Keywords' content='Web, html,  웹 표준' />
   <p>
     검색 엔진에 의해 검색되는 단어를 지정합니다.
   </p>
   
   <meta name="Description" content="Web, html, 웹 표준" />
   <p>
     검색 결과에 표시되는 문자를 지정합니다.
   </p>
   
   <meta name="Robots" content='noindex, nofollow' />
   <p>
     검색 로봇 제어
     content 속성에는 다음과 같이 지정할 수 있고 복수지정할 때에는 콤마(,)로 구분합니다.
   </p>
   <p>
     1. All(기본값): 'index, follow' 를 지정한 것과 같습니다.
   	2. None : 'noindex, nofollow' 를 지정한 것과 같습니다.
     3. Index : 그 페이지를 수집 대상으로 합니다.
   	4. Follow : 그 페이지를 포함해 링크가 걸린 곳을 수집 대상으로 합니다.
   	5. Noindex : 그 페이지를 수집대상에서 제외합니다.
     6. Nofollow : 그 페이지를 포함해 링크가 걸린 곳을 수집대상으로 하지 않습니다.
     Noarchive, Noimageindex, Noimageclick 등 웹 표준에선 인정하지 않는 속성도 있습니다.
   </p>
   
   <meta http-equiv="Content-Type" content='text/html; charset=utf-8' />
   <p>
     ISO-XXXX , EUC-kr 같은 문자 설정도 있지만 크기 설정에 제한이 있고 다국어 환경에서 호환이 되지 않기 때문에 유니코드 컨소시엄이 개발한 유니코드 표준인 UTF-8, UTF-16, UTF-32 선에서 정리되는 듯
   </p>
   
   <meta name="Date" content="2019-07-1ST07:00:00+09:00" />
   <p>
     content 설정 내 +09:00 은 GMT 로부터의 시차이며 +09:00 은 한국 미국 동부는 -05:00/-04:00(서머타임)
   </p>

   <meta http-equiv="Content-Script-Type" content="text/javascript" />
   <meta http-equiv="Content-Style-Type" content="text/css"/>
   <p>
    웹 페이지에 쓰인 언어를 지정합니다.
   </p>

   <meta http-equiv="X-UA-Compatible" content="IE=edge" />
   <p>
    브라우저 호환성을 지정함.
   </p>

   <meta http-equiv="Subject" content="웹 표준을 위한 사이트" />
   <p>
    홈페이지 주제를 지정
   </p>

   <meta http-equiv="Author" content="name">
   <p>
    페이지를 작성한 저자 지정
   </p>

   <meta http-equiv="Publisher" content="name">
   <p>
    제작사 지정
   </p>

   <meta http-equiv="Other Agent" content="name">
   <p>
    웹 책임자를 지정
   </p>

   <meta http-equiv="Generator" content="VS Code">
   <p>
    제작 도구를 지정
   </p>

   <meta http-equiv="Reply-To" content="reply@naver.com">
   <meta http-equiv="Email" content="a23842@naver.com">
   <p>
    이메일 주소를 지정
   </p>

   <meta http-equiv="Filename" content="index.html">
   <p>
    파일 이름을 지정
   </p>

   <meta http-equiv="Location" content="위치">
  <p>
    위치 지정
  </p>

  <meta http-equiv="Distribution" content="채찬우">
  <p>
    배포자를 지정
  </p>

  <meta http-equiv="Copyright" content="copyright@intern">
  <p>
    저작권을 지정
  </p>

  <meta http-equiv="Build" content="2019-07-01">
  <p>
    제작 년,월,일을 지정
  </p>

  <meta http-equiv="Last-Modified" content="Mon, 20 Jul 2016 19:30:30">
  <p>
    최종 수정일을 정의
  </p>

  <meta http-equiv="imagetoolbar" content="no">
  <p>
    그림 위에 마우스 오버 시 이미지 관련 툴바를 생기지 않도록 하기 위해 지정
  </p>

  <meta http-equiv="Cache-control" content="no-cache">
  <meta http-equiv="Pragma" content="no-cache">
  <p>
    캐쉬가 되지 않도록 하기 위해 정의
    페이지를 항상 서버에 접속해서 페이지를 가져오게 합니다.
    그러므로 방문자의 브라우저가 항상 cache를 읽도록 해놓아도 이것을 무시하고 페이지를 갱신합니다.
  </p>
  <p>
    자주 고치는 페이지에서는 이것을 사용해야 방문자에게 바뀌는 내용을 보여줄 수가 있습니다.
    하지만 페이지 출력 속도는 매번 페이지를 가져오기 때문에 시간이 많이 걸리는 단점이 있습니다.
  </p>
  
  <meta http-equiv="Expires" content="2019-07-01">
  <p>
    캐쉬 만료일을 지정
  </p>

  <meta http-equiv="Refresh" content="60">
  <p>
    60초마다 새로고침
  </p>

  <meta http-equiv="Page-Enter" content="revealtrans(Duration=1, Transition=12)">
  <p>
    페이지 들어갈 때 장면 전환 효과
  </p>
  <ul>
    <li>Box cut</li>
    <li>Circle in/out</li>
    <li>Wipe up/down/left/right</li>
    <li>Vertical/Horizontal blinds</li>
    <li>Checkerboard across <p>바둑판 형태의 격자가 왼쪽에서 오른쪽으로 생성</p></li>
    <li>Checkerboard down</li>
    <li>Random dissove <p>안개와 비슷한 형태로 전환</p></li>
    <li>Spilt vertical in<p>왼쪽과 오른쪽 끝에서 중앙으로 수직 이동</p></li>
    <li>Spilt Horizontal in<p>양쪽에서 중앙으로 수평 이동</p></li>
    <li>Spilt Horizontal out</li>
    <li>Strips left/right up/down</li>
    <li>Random bars horizontal/vertical</li>
    <li>Random</li>
  </ul>
   ```

   // naver webtoon meta 에 대해 indent 가 좀 이상함.