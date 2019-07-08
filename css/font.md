# font

``` css
/* 축약형 */
font: [font-style] [font-variant] [font-weight] [font-size/line height] [font-family] [initial|inherit]

font: oblique 2em '돋움', dotum, sans-serif;

font: oblique small-caps bold 16px/1.5 '돋움';

```



## 웹 폰트 / 시스템 폰트 / 이미지 폰트

 경우, 사람에 따라 여러 방식으로 불림

사용자의 로컬환경에 글꼴을 다운로드받아 적용하는 것

``` css
@font-face {
  font-family: webNanumGothic;
  src: url(NanumGothic.eot);
  font-weight: bold;
  font-style: italic;
}

body {
  font-family: webNanumGothic, 'sans-serif';
}
```

