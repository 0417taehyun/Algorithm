# Algorithm

## :books: Table Of Contents

- [Algorithm](#algorithm)
  - [:books: Table Of Contents](#books-table-of-contents)
    - [Team Note](#team-note)
    - [Programmers](#programmers)
      - [SQL](#sql)
      - [Python](#python)
    - [LeetCode](#leetcode)
      - [SQL](#sql-1)
      - [Python](#python-1)
    - [Baekjoon](#baekjoon)
      - [C](#c)
      - [Python](#python-2)
    - [이것이 취업을 위한 코딩 테스트다 with 파이썬](#이것이-취업을-위한-코딩-테스트다-with-파이썬)

### Team Note

<details>

<summary> 소스 코드 </summary>

<table>
    <tr>
        <th> 알고리즘 종류 </th> 
        <th> 알고리즘 한 줄 설명 </th>
        <th> C </th>
        <th> Java </th>
        <th> Python </th>
    </tr> 
    <tr>
        <td> 에라토스테네스의 체 </td>
        <td> 선형 시간에 근사하게 범위 내의 소수 구하기 </td>
        <td> <a href="./Team Note/C/eratos.c"> eratos.c </a> </td>
        <td> <a href=""> </a> </td>
        <td> <a href=""> </a> </td>
    </tr>
    <tr>
        <td> 퀵 정렬 - 1 </td>
        <td> 배열의 첫 번째 요소를 피봇의 기준으로 한 퀵 정렬 (이미 정렬이 된 최악의 경우 제곱 시간) </td>
        <td> <a href="./Team Note/C/quick_sort_1.c"> quick_sort_1.c </a> </td>
        <td> <a href=""> </a> </td>
        <td> <a href=""> </a> </td>
    </tr>
    <tr>
        <td> 서로소 집합 - 1 </td>
        <td> Quick Find 메서드로 구현한 UnionFind 자료구조 </td>
        <td> <a href=""> </a> </td>
        <td> <a href="./Team Note/disjoint_set_1.py"> disjoint_set_1.py </a> </td>
        <td> <a href=""> </a> </td>
    </tr>
    <tr>
        <td> 서로소 집합 - 2 </td>
        <td> Quick Union 메서드로 구현한 UnionFind 자료구조 </td>
        <td> <a href=""> </a> </td>
        <td> <a href="./Team Note/disjoint_set_2.py"> disjoint_set_2.py </a> </td>
        <td> <a href=""> </a> </td>
    </tr>
    <tr>
        <td> 서로소 집합 - 3 </td>
        <td> Union By Rank 방식으로 구현한 UnionFind 자료구조 </td>
        <td> <a href=""> </a> </td>
        <td> <a href="./Team Note/disjoint_set_3.py"> disjoint_set_3.py </a> </td>
        <td> <a href=""> </a> </td>
    </tr>
    <tr>
        <td> 서로소 집합 - 4 </td>
        <td> 경로 압축 최적화(Path Compression Optimization) 방식으로 구현한 UnionFind 자료구조 </td>
        <td> <a href=""> </a> </td>
        <td> <a href="./Team Note/disjoint_set_4.py"> disjoint_set_4.py </a> </td>
        <td> <a href=""> </a> </td>
    </tr>            
    <tr>
        <td> 서로소 집합 - 5 </td>
        <td> 경로 압축(Path Compression) 및 Union By Rank 방식을 통한 최적화하여 구현한 UnionFind 자료구조 </td>
        <td> <a href=""> </a> </td>
        <td> <a href="./Team Note/disjoint_set_5.py"> disjoint_set_5.py </a> </td>
        <td> <a href=""> </a> </td>
    </tr>    
    <tr>
        <td> 평방분할 (진행 중) </td>
        <td>  </td>
        <td> <a href=""> </a>  </td>
        <td> <a href=""> </a> </td>
        <td> <a href="./Team Note/Python/sqrt_decomposition.py"> sqrt_decomposition.py </a> </td>
    </tr>

</table>

</details>

### Programmers

#### SQL

<details>

<summary> LEVEL 1 </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59034"> 모든 레코드 조회하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/1.sql"> 1.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59415"> 최대값 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/2.sql"> 2.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59039"> 이름이 없는 동물의 아이디 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/3.sql"> 3.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59035"> 역순 정렬하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/4.sql"> 4.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59407"> 이름이 있는 동물의 아이디 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/5.sql"> 5.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59036#fn1"> 아픈 동물 찾기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/6.sql"> 6.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59037#fn1"> 어린 동물 찾기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/7.sql"> 7.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59403"> 동물의 아이디와 이름 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/8.sql"> 8.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59404"> 여러 기준으로 정렬하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/9.sql"> 9.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59405"> 상위 n개 레코드 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/10.sql"> 10.sql </a> </td>
    <td> 2021. 12. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131528"> 나이 정보가 없는 회원 수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/11.sql"> 11.sql </a> </td>
    <td> 2022. 10. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131112"> 강원도에 위치한 생산공장 목록 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/12.sql"> 12.sql </a> </td>
    <td> 2022. 10. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131114"> 경기도에 위치한 식품창고 목록 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/13.sql"> 13.sql </a> </td>
    <td> 2022. 10. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131697"> 가장 비싼 상품 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/14.sql"> 14.sql </a> </td>
    <td> 2022. 10. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131535"> 조건에 맞는 회원수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/15.sql"> 15.sql </a> </td>
    <td> 2022. 10. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/132203"> 흉부외과 또는 일반외과 의사 목록 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/16.sql"> 16.sql </a> </td>
    <td> 2022. 10. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/132201"> 12세 이하인 여자 환자 목록 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/17.sql"> 17.sql </a> </td>
    <td> 2022. 10. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/133024"> 인기있는 아이스크림 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/18.sql"> 18.sql </a> </td>
    <td> 2022. 10. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/133025"> 과일로 만든 아이스크림 고르기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/19.sql"> 19.sql </a> </td>
    <td> 2022. 10. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/144853"> 조건에 맞는 도서 리스트 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/20.sql"> 20.sql </a> </td>
    <td> 2022. 12. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/151136"> 평균 일일 대여 요금 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/21.sql"> 21.sql </a> </td>
    <td> 2023. 03. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/151138"> 자동차 대여 기록에서 장기/단기 대여 구분하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/22.sql"> 22.sql </a> </td>
    <td> 2023. 03. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/157343"> 특정 옵션이 포함된 자동차 리스트 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_1/23.sql"> 23.sql </a> </td>
    <td> 2023. 03. 04 </td>
</tr>
</table>

</details>

<details>

<summary> LEVEL 2 </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59040"> 고양이와 개는 몇 마리 있을까 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/1.sql"> 1.sql </a> </td>
    <td> 2022. 03. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59046"> 루시와 엘라 찾기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/2.sql"> 2.sql </a> </td>
    <td> 2022. 03. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59038"> 최솟값 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/3.sql"> 3.sql </a> </td>
    <td> 2022. 03. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59041"> 동명 동물 수 찾기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/4.sql"> 4.sql </a> </td>
    <td> 2022. 03. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59047"> 이름에 el이 들어가는 동물 찾기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/5.sql"> 5.sql </a> </td>
    <td> 2022. 03. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59406"> 동물 수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/6.sql"> 6.sql </a> </td>
    <td> 2022. 03. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59412"> 입양 시각 구하기(1) </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/7.sql"> 7.sql </a> </td>
    <td> 2022. 03. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59410"> NULL 처리하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/8.sql"> 8.sql </a> </td>
    <td> 2022. 03. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59409"> 중성화 여부 파악하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/9.sql"> 9.sql </a> </td>
    <td> 2022. 03. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59408"> 중복 제거하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/10.sql"> 10.sql </a> </td>
    <td> 2022. 03. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59414"> DATETIME에서 DATE로 형 변환 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/11.sql"> 11.sql </a> </td>
    <td> 2022. 03. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131115#"> 가격이 제일 비싼 식품의 정보 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/12.sql"> 12.sql </a> </td>
    <td> 2022. 10. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/132202"> 진료과별 총 예약 횟수 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/13.sql"> 13.sql </a> </td>
    <td> 2022. 10. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131529"> 카테고리 별 상품 개수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/14.sql"> 14.sql </a> </td>
    <td> 2022. 10. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131533"> 상품 별 오프라인 매출 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/15.sql"> 15.sql </a> </td>
    <td> 2022. 10. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131120"> 3월에 태어난 여성 회원 목록 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/16.sql"> 16.sql </a> </td>
    <td> 2022. 10. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/133026"> 성분으로 구분한 아이스크림 총 주문량 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/17.sql"> 17.sql </a> </td>
    <td> 2022. 10. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131536"> 재구매가 일어난 상품과 회원 리스트 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/18.sql"> 18.sql </a> </td>
    <td> 2022. 10. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131530"> 가격대 별 상품 개수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/19.sql"> 19.sql </a> </td>
    <td> 2022. 10. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/144854"> 조건에 맞는 도서와 저자 리스트 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/20.sql"> 20.sql </a> </td>
    <td> 2022. 12. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/151137"> 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/21.sql"> 21.sql </a> </td>
    <td> 2023. 03. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/157342"> 자동차 평균 대여 기간 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_2/22.sql"> 22.sql </a> </td>
    <td> 2023. 03. 05 </td>
</tr>
</table>

</details>

<details>

<summary> LEVEL 3 </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59042"> 없어진 기록 찾기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/1.sql"> 1.sql </a> </td>
    <td> 2022. 03. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59043"> 있었는데요 없었습니다 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/2.sql"> 2.sql </a> </td>
    <td> 2022. 03. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59044"> 오랜 기간 보호한 동물(1) </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/3.sql"> 3.sql </a> </td>
    <td> 2022. 03. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59411"> 오랜 기간 보호한 동물(2) </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/4.sql"> 4.sql </a> </td>
    <td> 2022. 03. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/77487"> 헤비 유저가 소유한 장소 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/5.sql"> 5.sql </a> </td>
    <td> 2022. 03. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131123"> 즐겨찾기가 가장 많은 식당 정보 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/6.sql"> 6.sql </a> </td>
    <td> 2022. 10. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131113"> 조건별로 분류하여 주문상태 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/7.sql"> 7.sql </a> </td>
    <td> 2022. 10. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/144855"> 카테고리 별 도서 판매량 집계하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/8.sql"> 8.sql </a> </td>
    <td> 2022. 12. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/151139"> 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/9.sql"> 9.sql </a> </td>
    <td> 2023. 03. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/157341"> 대여 기록이 존재하는 자동차 리스트 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/10.sql"> 10.sql </a> </td>
    <td> 2023. 03. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/157340"> 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_3/11.sql"> 11.sql </a> </td>
    <td> 2023. 03. 06 </td>
</tr>
</table>

</details>

<details>

<summary> LEVEL 4 </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/62284"> 우유와 요거트가 담긴 장바구니 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/1.sql"> 1.sql </a> </td>
    <td> 2022. 03. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59413"> 입양 시각 구하기(2) </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/2.sql"> 2.sql </a> </td>
    <td> 2022. 03. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://programmers.co.kr/learn/courses/30/lessons/59045"> 보호소에서 중성화한 동물 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/3.sql"> 3.sql </a> </td>
    <td> 2022. 03. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131117"> 5월 식품들의 총매출 조회하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/4.sql"> 4.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131116"> 식품분류별 가장 비싼 식품의 정보 조회하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/5.sql"> 5.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/133027"> 주문량이 많은 아이스크림들 조회하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/6.sql"> 6.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131118"> 서울에 위치한 식당 목록 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/7.sql"> 7.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131532"> 년, 월, 성별 별 상품 구매 회원 수 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/8.sql"> 8.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/132204"> 취소되지 않은 진료 예약 조회하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/9.sql"> 9.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131537"> 오프라인/온라인 판매 데이터 통합하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/10.sql"> 10.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131124"> 그룹별 조건에 맞는 식당 목록 출력하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/11.sql"> 11.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/144856"> 카테고리 별 도서 판매량 집계하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/12.sql"> 12.sql </a> </td>
    <td> 2022. 12. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/151141"> 자동차 대여 기록 별 대여 금액 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/13.sql"> 13.sql </a> </td>
    <td> 2023. 03. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/157339"> 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_4/14.sql"> 14.sql </a> </td>
    <td> 2023. 03. 07 </td>
</tr>
</table>

</details>

<details>

<summary> LEVEL 5 </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/131534"> 상품을 구매한 회원 비율 구하기 </a> </td>
    <td> <a href="./Programmers/SQL/LEVEL_5/1.sql"> 1.sql </a> </td>
    <td> 2022. 10. 30 </td>
</tr>
</table>

</details>

#### Python

<details>

<summary> LEVEL 3 </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://school.programmers.co.kr/learn/courses/30/lessons/43238"> 입국심사 </a> </td>
    <td> <a href="./Programmers/Python/LEVEL_3/43238.py"> 43238.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/alogrithm-programmers-43238"> [ 알고리즘 ] 프로그래머스: 입국심사 </a> </td>
    <td> 2022. 08. 01 </td>
</tr>
</table>

</details>

### LeetCode

#### SQL

<details>

<summary> Easy </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/employees-earning-more-than-their-managers/"> 181. Employess Earning More Than Their Managers </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/181.sql"> 181.sql </a></td>
    <td> 2022. 03. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/duplicate-emails/"> 182. Duplicate Emails </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/182"> 182.sql </a> </td>
    <td> 2022. 03. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/customers-who-never-order/"> 183. Customers Who Never Order </a></td>
    <td> <a href="/LeetCode/SQL/1_Easy/183.sql"> 183.sql </a></td>
    <td> 2022. 03. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/delete-duplicate-emails/"> 196. Delete Duplicate Emails </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/196.sql"> 196.sql </td>
    <td> 2022. 03. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/rising-temperature/"> 197. Rising Temperature </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/197.sql"> 197.sql </a> </td>
    <td> 2022. 03. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/game-play-analysis-i/"> 511. Game Play Analysis I </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/511.sql"> 511.sql </a> </td>
    <td> 2022. 03. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/game-play-analysis-ii/"> 512. Game Play Analysis II </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/512.sql"> 512.sql </a> </td>
    <td> 2022. 03. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/employee-bonus/"> 577. Employee Bonus </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/577.sql"> 577.sql </a> </td>
    <td> 2022. 03. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-customer-referee/"> 584. Find Customer Referee </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/584.sql"> 584.sql </a> </td>
    <td> 2022. 03. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/"> 586. Customer Placing the Largest Number of Orders </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/586.sql"> 586.sql </a> </td>
    <td> 2022. 03. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/big-countries/"> 595. Big Countries </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/595.sql"> 595.sql </a> </td>
    <td> 2022. 03. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/classes-more-than-5-students/"> 596. Classes More Than 5 Students </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/596.sql"> 596.sql </a> </td>
    <td> 2022. 03. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/"> 597. Friend Requests I: Overall Acceptance Rate </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/597.sql"> 597.sql </a> </td>
    <td> 2022. 03. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/consecutive-available-seats/"> 603. Consecutive Available Seats </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/603.sql"> 603.sql </a> </td>
    <td> 2022. 03. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sales-person/"> 607. Sales Person </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/607.sql"> 607.sql </a> </td>
    <td> 2022. 03. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/triangle-judgement/"> 610. Triangle Judgement </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/610.sql"> 610.sql </a> </td>
    <td> 2022. 03. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/shortest-distance-in-a-line/"> 613. Shortest Distance in a Line </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/613.sql"> 613.sql </a> </td>
    <td> 2022. 03. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/biggest-single-number/"> 619. Biggest Single Number </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/619.sql"> 619.sql </a> </td>
    <td> 2022. 03. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/not-boring-movies/"> 620. Not Boring Movies </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/620.sql"> 620.sql </a> </td>
    <td> 2022. 03. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/swap-salary/"> 627. Swap Salary </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/627.sql"> 627.sql </a> </td>
    <td> 2022. 03. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/"> 1050. Actors and Directors Who Cooperated At Least Three Times </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1050.sql"> 1050.sql </a> </td>
    <td> 2022. 03. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/product-sales-analysis-i/"> 1068. Product Sales Analysis I </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1068.sql"> 1068.sql </a> </td>
    <td> 2022. 03. 27 </td>
</tr>
<tr>
    <td> <a href="https://leetcode.com/problems/product-sales-analysis-ii/"> 1069. Product Sales Analysis II </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1069.sql"> 1069.sql </a> </td>
    <td> 2022. 03. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/project-employees-i/"> 1075. Project Employees I </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1075.sql"> 1075.sql </a> </td>
    <td> 2022. 03. 2 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/project-employees-ii/"> 1076. Project Employees II </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1076.sql"> 1076.sql </a> </td>
    <td> 2022. 03. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sales-analysis-i/"> 1082. Sales Analysis I </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1082.sql"> 1082.sql </a> </td>
    <td> 2022. 03. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sales-analysis-ii/"> 1083. Sales Analysis II </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1083.sql"> 1083.sql </a> </td>
    <td> 2022. 03. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sales-analysis-iii/"> 1084. Sales Analysis III </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1084.sql"> 1084.sql </a> </td>
    <td> 2022. 03. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reported-posts/"> 1113. Reported Posts </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1113.sql"> 1113.sql </a> </td>
    <td> 2022. 03. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/user-activity-for-the-past-30-days-i/"> 1141. User Activity for the Past 30 Days I </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1141.sql"> 1141.sql </a> </td>
    <td> 2022. 03. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/"> 1142. User Activity for the Past 30 Days II </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1142.sql"> 1142.sql </a> </td>
    <td> 2022. 03. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/article-views-i/"> 1148. Article Views I </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1148.sql"> 1148.sql </a> </td>
    <td> 2022. 03. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/immediate-food-delivery-i/"> 1173. Immediate Food Delivery I </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1173.sql"> 1173.sql </a> </td>
    <td> 2022. 03. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reformat-department-table/"> 1179. Reformat Department Table </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1179.sql"> 1179.sql </a> </td>
    <td> 2022. 03. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/queries-quality-and-percentage/"> 1211. Queries Quality and Percentage </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1211.sql"> 1211.sql </a> </td>
    <td> 2022. 03. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-comments-per-post/"> 1241. Number of Comments per Post </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1241.sql"> 1241.sql </a> </td>
    <td> 2022. 03. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/average-selling-price/"> 1251. Average Selling Price </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1251.sql"> 1251.sql </a> </td>
    <td> 2022. 03. 31 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-the-team-size/"> 1303. Find the Team Size </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1303.sql"> 1303.sql </a> </td>
    <td> 2022. 04. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/weather-type-in-each-country/"> 1294. Weather Type in Each Country </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1294.sql"> 1294.sql </a> </td>
    <td> 2022. 04. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/students-and-examinations/"> 1280. Students and Examinations </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1280.sql"> 1280.sql </a> </td>
    <td> 2022. 04. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/ads-performance/"> 1322. Ads Performance </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1322.sql"> 1322.sql </a> </td>
    <td> 2022. 04. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/list-the-products-ordered-in-a-period/"> 1327. List the Products Ordered in a Period </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1327.sql"> 1327.sql </a> </td>
    <td> 2022. 04. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/students-with-invalid-departments/"> 1350. Students With Invalid Departments </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1350.sql"> 1350.sql </a> </td>
    <td> 2022. 04. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/"> 1378. Replace Employee ID With The Unique Identifier </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1378.sql"> 1378.sql </a> </td>
    <td> 2022. 04. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/top-travellers/"> 1407. Top Travellers </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1407.sql"> 1407.sql </a> </td>
    <td> 2022. 04. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/npv-queries/"> 1421. NPV Queries </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1421.sql"> 1421.sql </a> </td>
    <td> 2022. 04. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/create-a-session-bar-chart/"> 1435. Create a Session Bar Chart </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1435.sql"> 1435.sql </a> </td>
    <td> 2022. 04. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/group-sold-products-by-the-date/"> 1484. Group Sold Products By The Date </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1484.sql"> 1484.sql </a> </td>
    <td> 2022. 04. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/friendly-movies-streamed-last-month/"> 1495. Friendly Movies Streamed Last Month </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1495.sql"> 1495.sql </a> </td>
    <td> 2022. 04. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/customer-order-frequency/"> 1511. Customer Order Frequency </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1511.sql"> 1511.sql </a> </td>
    <td> 2022. 04. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-users-with-valid-e-mails/"> 1517. Find Users With Valid E-Mails </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1517.sql"> 1517.sql </a> </td>
    <td> 2022. 04. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/patients-with-a-condition/"> 1527. Patients With a Condition </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1527.sql"> 1527.sql </a> </td>
    <td> 2022. 04. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/fix-product-name-format/"> 1543. Fix Product Name Format </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1543.sql"> 1543.sql </a> </td>
    <td> 2022. 04. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/unique-orders-and-customers-per-month/"> 1565. Unique Orders and Customers Per Month </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1565.sql"> 1565.sql </a> </td>
    <td> 2022. 04. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/warehouse-manager/"> 1571. Warehouse Manager </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1571.sql"> 1571.sql </a> </td>
    <td> 2022. 04. 13 </td>
</tr>
<tr align="left">
    <td><a href="https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/"> 1581. Customer Who Visited but Did Not Make Any Transactions </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1581.sql"> 1581.sql </a> </td>
    <td> 2022. 04. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/bank-account-summary-ii/"> 1587. Bank Account Summary II </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1587.sql"> 1587.sql </a> </td>
    <td> 2022. 04. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sellers-with-no-sales/"> 1607. Sellers With No Sales </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1607.sql"> 1607.sql </a> </td>
    <td> 2022. 04. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/"> 1623. All Valid Triplets That Can Represent a Country </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1623.sql"> 1623.sql </a> </td>
    <td> 2022. 04. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/percentage-of-users-attended-a-contest/"> 1633. Percentage of Users Attended a Contest </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1633.sql"> 1633.sql </a> </td>
    <td> 2022. 04. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/average-time-of-process-per-machine/"> 1661. Average Time of Process per Machine </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1661.sql"> 1661.sql </a> </td>
    <td> 2022. 04. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/fix-names-in-a-table/"> 1667. Fix Names in a Table </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1667.sql"> 1667.sql </a> </td>
    <td> 2022. 04. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/products-worth-over-invoices/"> 1677. Product's Worth Over Invoices </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1677.sql"> 1677.sql </a> </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/invalid-tweets/"> 1683. Invalid Tweets </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1683.sql"> 1683.sql </a> </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/daily-leads-and-partners/"> 1693. Daily Leads and Partners </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1693.sql"> 1693.sql </a> </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-followers-count/"> 1729. Find Followers Count </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1729.sql"> 1729.sql </a> </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/"> 1731. The Number of Employees Which Report to Each Employee </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1731.sql"> 1731.sql </a> </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-total-time-spent-by-each-employee/"> 1741. Find Total Time Spent by Each Employee </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1741.sql"> 1741.sql </a>  </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/recyclable-and-low-fat-products/"> 1757. Recyclable and Low Fat Products </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1757.sql"> 1757.sql </a> </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/products-price-for-each-store/"> 1777. Product's Price for Each Store </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1777.sql"> 1777.sql </a> </td>
    <td> 2022. 04. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/primary-department-for-each-employee/"> 1789. Primary Department for Each Employee </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1789.sql"> 1789.sql </a> </td>
    <td> 2022. 04. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/rearrange-products-table/"> 1795. Rearrange Products Table </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1795.sql"> 1795.sql </a> </td>
    <td> 2022. 04. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/ad-free-sessions/"> 1809. Ad-Free Sessions </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1809.sql"> 1809.sql </a> </td>
    <td> 2022. 04. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/"> 1821. Find Customers With Positive Revenue this Year </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1821.sql"> 1821.sql </a> </td>
    <td> 2022. 04. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/convert-date-format/"> 1853. Convert Date Format </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1853.sql"> 1853.sql </a> </td>
    <td> 2022. 04. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/calculate-special-bonus/"> 1873. Calculate Special Bonus </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1873.sql"> 1873.sql </a> </td>
    <td> 2022. 04. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-latest-login-in-2020/"> 1890. The Latest Login in 2020 </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1890.sql"> 1890.sql </a> </td>
    <td> 2022. 04. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/users-that-actively-request-confirmation-messages/"> 1939. Users That Actively Request Confirmation Messages </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1939.sql"> 1939.sql </a> </td>
    <td> 2022. 04. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/employees-with-missing-information/"> 1965. Employees With Missing Information </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1965.sql"> 1965.sql </a> </td>
    <td> 2022. 04. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/employees-whose-manager-left-the-company/"> 1978. Employees Whose Manager Left the Company </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/1978.sql"> 1978.sql </a> </td>
    <td> 2022. 04. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/low-quality-problems/"> 2026. Low-Quality Problems </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2026.sql"> 2026.sql </a> </td>
    <td> 2022. 04. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-winner-university/"> 2072. The Winner University </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2072.sql"> 2072.sql </a> </td>
    <td> 2022. 04. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-rich-customers/"> 2082. The Number of Rich Customers </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2082.sql"> 2082.sql </a> </td>
    <td> 2022. 04. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/"> 2205. The Number of Users That Are Eligible for Discount </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2205.sql"> 2205.sql </a> </td>
    <td> 2022. 04. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-users-that-are-eligible-for-discount/"> 2230. The Users That Are Eligible for Discount </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2230.sql"> 2230.sql </a> </td>
    <td> 2022. 04. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/all-the-matches-of-the-league/"> 2239. All the Matches of the League </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2339.sql"> 2339.sql </a> </td>
    <td> 2022. 07. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/compute-the-rank-as-a-percentage/"> 2346. Compute the Rank as a Percentage </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2346.sql"> 2346.sql </a> </td>
    <td> 2022. 07. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/"> 2356. Number of Unique Subjects Taught by Each Teacher </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2356.sql"> 2356.sql </a> </td>
    <td> 2022. 07. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sort-the-olympic-table/"> 2377. Sort the Olympic Table </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2377.sql"> 2377.sql </a> </td>
    <td> 2022. 08. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/form-a-chemical-bond/description/"> 2480. Form a Chemical Bond </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2480.sql"> 2480.sql </a> </td>
    <td> 2022. 12. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/concatenate-the-name-and-the-profession/description/"> 2504. Concatenate the Name and the Profession </a> </td>
    <td> <a href="./LeetCode/SQL/1_Easy/2504.sql"> 2504.sql </a> </td>
    <td> 2022. 12. 12 </td>
</tr>
</table>

</details>

<details>

<summary> Medium </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/second-highest-salary/"> 176. Second Highest Salary </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/176.sql"> 176.sql </a> </td>
    <td> 2022. 04. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/nth-highest-salary/"> 177. Nth Highest Salary </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/177.sql"> 177.sql </a> </td>
    <td> 2022. 04. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/rank-scores/"> 178. Rank Scores </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/178.sql"> 178.sql </a> </td>
    <td> 2022. 04. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/consecutive-numbers/"> 180. Consecutive Numbers </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/180.sql"> 180.sql </a> </td>
    <td> 2022. 04. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/department-highest-salary/"> 184. Department Highest Salary </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/184.sql"> 184.sql </a> </td>
    <td> 2022. 04. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/game-play-analysis-iii/"> 534. Game Play Analysis III </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/534.sql"> 534.sql </a> </td>
    <td> 2022. 04. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/game-play-analysis-iv/"> 550. Game Play Analysis IV </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/550.sql"> 550.sql </a> </td>
    <td> 2022. 04. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/managers-with-at-least-5-direct-reports/"> 570. Managers with at Least 5 Direct Reports </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/570.sql"> 570.sql </a> </td>
    <td> 2022. 04. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/winning-candidate/"> 574. Winning Candidate </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/574.sql"> 574.sql </a> </td>
    <td> 2022. 04. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/get-highest-answer-rate-question/"> 578. Get Highest Answer Rate Question </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/578.sql"> 578.sql </a> </td>
    <td> 2022. 04. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/count-student-number-in-departments/"> 580. Count Student Number in Departments </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/580.sql"> 580.sql </a> </td>
    <td> 2022. 04. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/investments-in-2016/"> 585. Investments in 2016 </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/585.sql"> 585.sql </a> </td>
    <td> 2022. 04. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/"> 602. Friend Requests II: Who Has the Most Friends </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/602.sql"> 602.sql </a> </td>
    <td> 2022. 04. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/tree-node/"> 608. Tree Node </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/608.sql"> 608.sql </a> </td>
    <td> 2022. 04. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/shortest-distance-in-a-plane/"> 612. Shortest Distance in a Plane </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/612.sql"> 612.sql </a> </td>
    <td> 2022. 04. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/second-degree-follower/"> 614. Second Degree Follower </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/614.sql"> 614.sql </a> </td>
    <td> 2022. 04. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/exchange-seats/"> 626. Exchange Seats </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/626.sql"> 626.sql </a> </td>
    <td> 2022. 04. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/customers-who-bought-all-products/"> 1045. Customers Who Bought All Products </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1045.sql"> 1045.sql </a> </td>
    <td> 2022. 05. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/product-sales-analysis-iii/"> 1070. Product Sales Analysis III </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1070.sql"> 1070.sql </a> </td>
    <td> 2022. 05. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/project-employees-iii/"> 1077. Project Employees III </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1077.sql"> 1077.sql </a> </td>
    <td> 2022. 05. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/unpopular-books/"> 1098. Unpopular Books </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1098.sql"> 1098.sql </a> </td>
    <td> 2022. 05. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/new-users-daily-count/"> 1107. New Users Daily Count </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1107.sql"> 1107.sql </a> </td>
    <td> 2022. 05. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/highest-grade-for-each-student/"> 1112. Highest Grade For Each Student </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1112.sql"> 1112.sql </a> </td>
    <td> 2022. 05. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/active-businesses/"> 1126. Active Businesses </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1126.sql"> 1126.sql </a> </td>
    <td> 2022. 05. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reported-posts-ii/"> 1132. Reported Posts II </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1132.sql"> 1132.sql </a> </td>
    <td> 2022. 05. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/article-views-ii/"> 1149. Article Views II </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1149.sql"> 1149.sql </a> </td>
    <td> 2022. 05. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/market-analysis-i/"> 1158. Market Analysis I </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1158.sql"> 1158.sql </a> </td>
    <td> 2022. 05. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/product-price-at-a-given-date/"> 1164. Product Price at a Given Date </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1164.sql"> 1164.sql </a> </td>
    <td> 2022. 05. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/immediate-food-delivery-ii/"> 1174. Immediate Food Delivery II </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1174.sql"> 1174.sql </a> </td>
    <td> 2022. 05. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/monthly-transactions-i/"> 1193. Monthly Transactions I </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1193.sql"> 1193.sql </a> </td>
    <td> 2022. 05. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/last-person-to-fit-in-the-bus/"> 1204. Last Person to Fit in the Bus </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1204.sql"> 1204.sql </a> </td>
    <td> 2022. 05. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/monthly-transactions-ii/"> 1205. Monthly Transactions II </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1205.sql"> 1205.sql </a> </td>
    <td> 2022. 05. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/team-scores-in-football-tournament/"> 1212. Team Scores in Football Tournament </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1212.sql"> 1212.sql </a> </td>
    <td> 2022. 05. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/page-recommendations/"> 1264. Page Recommendations </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1264.sql"> 1264.sql </a> </td>
    <td> 2022. 05. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/running-total-for-different-genders/"> 1308. Running Total for Different Genders </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1308.sql"> 1308.sql </a> </td>
    <td> 2022. 05. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/"> 1285. Find the Start and End Number of Continuous Ranges </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1285.sql"> 1285.sql </a> </td>
    <td> 2022. 05. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/restaurant-growth/"> 1321. Restaurant Growth </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1321.sql"> 1321.sql </a> </td>
    <td> 2022. 05. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/movie-rating/"> 1341. Movie Rating </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1341.sql"> 1341.sql </a> </td>
    <td> 2022. 05. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/activity-participants/"> 1355. Activity Participants </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1355.sql"> 1355.sql </a> </td>
    <td> 2022. 05. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/"> 1364. Number of Trusted Contacts of a Customer </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1364.sql"> 1364.sql </a> </td>
    <td> 2022. 05. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/capital-gainloss/"> 1393. Capital Gain/Loss </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1393.sql"> 1393.sql </a> </td>
    <td> 2022. 05. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/"> 1398. Customers Who Bought Products A and B but Not C </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1398.sql"> 1398.sql </a> </td>
    <td> 2022. 05. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/evaluate-boolean-expression/"> 1440. Evaluate Boolean Expression </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1440.sql"> 1440.sql </a> </td>
    <td> 2022. 05. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/apples-oranges/"> 1445. Apples &amp; Oranges </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1445.sql"> 1445.sql </a> </td>
    <td> 2022. 05. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/active-users/"> 1454. Active Users </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1454.sql"> 1454.sql </a> </td>
    <td> 2022. 05. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/calculate-salaries/"> 1468. Calculate Salaries </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1468.sql"> 1468.sql </a> </td>
    <td> 2022. 05. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/countries-you-can-safely-invest-in/"> 1501. Countries You Can Safely Invest In </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1501.sql"> 1501.sql </a> </td>
    <td> 2022. 05. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-most-recent-three-orders/"> 1532. The Most Recent Three Orders </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1532.sql"> 1532.sql </a> </td>
    <td> 2022. 05. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-most-recent-orders-for-each-product/"> 1549. The Most Recent Orders for Each Product </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1549.sql"> 1549.sql </a> </td>
    <td> 2022. 05. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/bank-account-summary/"> 1555. Bank Account Summary </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1555.sql"> 1555.sql </a> </td>
    <td> 2022. 05. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/"> 1596. The Most Frequently Ordered Products for Each Customer </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1596.sql"> 1596.sql </a> </td>
    <td> 2022. 05. 19 </td>
</tr>
<tr>
    <td> <a href="https://leetcode.com/problems/find-the-missing-ids/"> 1613. Find the Missing IDs </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1613.sql"> 1613.sql </a> </td>
    <td> 2022. 05. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-calls-between-two-persons/"> 1699. Number of Calls Between Two Persons </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1699.sql"> 1699.sql </a> </td>
    <td> 2022. 05. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/biggest-window-between-visits/"> 1709. Biggest Window Between Visits </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1709.sql"> 1709.sql </a> </td>
    <td> 2022. 05. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/count-apples-and-oranges/"> 1715. Count Apples and Oranges </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1715.sql"> 1715.sql </a> </td>
    <td> 2022. 05. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/leetflex-banned-accounts/"> 1747. Leetflex Banned Accounts </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1747.sql"> 1747.sql </a> </td>
    <td> 2022. 05. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/grand-slam-titles/"> 1783. Grand Slam Titles </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1783.sql"> 1783.sql </a> </td>
    <td> 2022. 05. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-interview-candidates/"> 1811. Find Interview Candidates </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1811.sql"> 1811.sql </a> </td>
    <td> 2022. 05. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-transaction-each-day/submissions/"> 1831. Maximum Transaction Each Day </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1831.sql"> 1831.sql </a> </td>
    <td> 2022. 05. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/league-statistics/"> 1841. League Statistics </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1841.sql"> 1841.sql </a> </td>
    <td> 2022. 05. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/suspicious-bank-accounts/"> 1843. Suspicious Bank Accounts </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1843.sql"> 1843.sql </a> </td>
    <td> 2022. 05. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/orders-with-maximum-quantity-above-average/"> 1867. Orders With Maximum Quantity Above Average </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1867.sql"> 1867.sql </a> </td>
    <td> 2022. 05. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/group-employees-of-the-same-salary/"> 1875. Group Employees of the Same Salary </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1875.sql"> 1875.sql </a> </td>
    <td> 2022. 05. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/count-salary-categories/submissions/"> 1907. Count Salary Categories </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1907.sql"> 1907.sql </a> </td>
    <td> 2022. 05. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/confirmation-rate/"> 1934. Confirmation Rate </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1934.sql"> 1934.sql </a> </td>
    <td> 2022. 05. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-cutoff-score-for-each-school/"> 1988. Find Cutoff Score for Each School </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1988.sql"> 1988.sql </a> </td>
    <td> 2022. 05. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/rectangles-area/submissions/"> 1459. Rectangles Area </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1459.sql"> 1459.sql </a> </td>
    <td> 2022. 05. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/"> 1951. All the Pairs With the Maximum Number of Common Followers </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1951.sql"> 1951.sql </a> </td>
    <td> 2022. 05. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/all-people-report-to-the-given-manager/"> 1270. All People Report to the Given Manager </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1270.sql"> 1270.sql </a> </td>
    <td> 2022. 05. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/strong-friendship/"> 1949. Strong Friendship </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1949.sql"> 1949.sql </a> </td>
    <td> 2022. 05. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/count-the-number-of-experiments/"> 1990. Count the Number of Experiments </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/1990.sql"> 1990.sql </a> </td>
    <td> 2022. 05. 31 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-accounts-that-did-not-stream/"> 2020. Number of Accounts That Did Not Stream </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2020.sql"> 2020.sql </a> </td>
    <td> 2022. 05. 31 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/accepted-candidates-from-the-interviews/"> 2041. Accepted Candidates From the Interviews </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2041.sql"> 2041.sql </a> </td>
    <td> 2022. 06. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-category-of-each-member-in-the-store/"> 2051. The Category of Each Member in the Store </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2051.sql"> 2051.sql </a> </td>
    <td> 2022. 06. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/account-balance/"> 2066. Account Balance </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2066.sql"> 2066.sql </a> </td>
    <td> 2022. 06. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/"> 2084. Drop Type 1 Orders for Customers With Type 0 Orders </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2084.sql"> 2084.sql </a> </td>
    <td> 2022. 06. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-airport-with-the-most-traffic/"> 2112. The Airport With the Most Traffic </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2112.sql"> 2112.sql </a> </td>
    <td> 2022. 06. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/"> 2142. The Number of Passengers in Each Bus I </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2142.sql"> 2142.sql </a> </td>
    <td> 2022. 06. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/order-two-columns-independently/"> 2159. Order Two Columns Independently </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2159.sql"> 2159.sql </a> </td>
    <td> 2022. 06. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-change-in-global-rankings/"> 2175. The Change in Global Rankings </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2175.sql"> 2175.sql </a> </td>
    <td> 2022. 06. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/users-with-two-purchases-within-seven-days/"> 2228. Users With Two Purchases Within Seven Days </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2228.sql"> 2228.sql </a> </td>
    <td> 2022. 06. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/"> 2238. Number of Times a Driver Was a Passenger </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2238.sql"> 2238.sql </a> </td>
    <td> 2022. 06. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/"> 2292. Products With Three or More Orders in Two Consecutive Years </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2292.sql"> 2292.sql </a> </td>
    <td> 2022. 06. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/tasks-count-in-the-weekend/"> 2298. Tasks Count in the Weekend </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2298.sql"> 2298.sql </a> </td>
    <td> 2022. 06. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/arrange-table-by-gender/"> 2308. Arrange Table by Gender </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2308.sql"> 2308.sql </a> </td>
    <td> 2022. 06. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/"> 2314. The First Day of the Maximum Recorded Degree in Each City </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2314.sql"> 2314.sql </a> </td>
    <td> 2022. 06. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/product-sales-analysis-iv/"> 2324. Product Sales Analysis IV </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2324.sql"> 2324.sql </a> </td>
    <td> 2022. 07. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/product-sales-analysis-v/"> 2329. Product Sales Analysis V </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2329.sql"> 2329.sql </a> </td>
    <td> 2022. 07. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/calculate-the-influence-of-each-salesperson/"> 2372. Calculate the Influence of Each Salesperson </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2372.sql"> 2372.sql </a> </td>
    <td> 2022. 08. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/"> 2388. Change Null Values in a Table to the Previous Value </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2388.sql"> 2388.sql </a> </td>
    <td> 2022. 08. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/employees-with-deductions/"> 2394. Employees With Deductions </a> </td>
    <td> <a href="./LeetCode/SQL/2_Medium/2394.sql"> 2394.sql </a> </td>
    <td> 2022. 09. 03 </td>
</tr>
</table>

</details>

<details>

<summary> Hard </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/department-top-three-salaries/"> 185. Department Top Three Salaries </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/185.sql"> 185.sql </a> </td>
    <td> 2022. 05. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/trips-and-users/"> 262. Trips and Users </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/262.sql"> 262.sql </a> </td>
    <td> 2022. 05. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/get-the-second-most-recent-activity/"> 1369. Get the Second Most Recent Activity </a></td>
    <td> <a href="./LeetCode/SQL/3_Hard/1369.sql"> 1369.sql </a> </td>
    <td> 2022. 06. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-the-quiet-students-in-all-exams/"> 1412. Find the Quiet Students in All Exams </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1412.sql"> 1412.sql </a> </td>
    <td> 2022. 06. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/first-and-last-call-on-the-same-day/"> 1972. First and Last Call On the Same Day </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1972.sql"> 1972.sql </a> </td>
    <td> 2022. 06. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/"> 1767. Find the Subtasks That Did Not Execute </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1767.sql"> 1767.sql </a> </td>
    <td> 2022. 06. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/median-employee-salary/"> 569. Median Employee Salary </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/569.sql"> 569.sql </a> </td>
    <td> 2022. 06. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/total-sales-amount-by-year/"> 1384. Total Sales Amount by Year </a> </td>
    <td> <a href="LeetCode/SQL/3_Hard/1384.sql"> 1384.sql </a> </td>
    <td> 2022. 06. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-median-given-frequency-of-numbers/"> 571. Find Median Given Frequency of Numbers </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/571.sql"> 571.sql </a> </td>
    <td> 2022. 06. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/report-contiguous-dates/"> 1225. Report Contiguous Dates </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1225.sql"> 1225.sql </a> </td>
    <td> 2022. 06. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/students-report-by-geography/"> 618. Students Report By Geography </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/618.sql"> 618.sql </a> </td>
    <td> 2022. 06. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company-ii/submissions/"> 2010. The Number of Seniors and Juniors to Join the Company II </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2010.sql"> 2010.sql </a> </td>
    <td> 2022. 06. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-cumulative-salary-of-an-employee/"> 579. Find Cumulative Salary of an Employee </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/579.sql"> 579.sql </a> </td>
    <td> 2022. 06. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/human-traffic-of-stadium/"> 601. Human Traffic of Stadium </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/601.sql"> 601.sql </a> </td>
    <td> 2022. 06. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/average-salary-departments-vs-company/"> 615. Average Salary: Departments VS Company </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/615.sql"> 615.sql </a> </td>
    <td> 2022. 06. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/game-play-analysis-v/)"> 1097. Game Play Analysis V </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1097.sql"> 1097.sql </a> </td>
    <td> 2022. 06. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/user-purchase-platform/"> 1127. User Purchase Platform </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1127.sql"> 1127.sql </a> </td>
    <td> 2022. 06. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/market-analysis-ii/"> 1159. Market Analysis II </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1159.sql"> 1159.sql </a> </td>
    <td> 2022. 06. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/tournament-winners/"> 1194. Tournament Winners </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1194.sql"> 1194.sql </a> </td>
    <td> 2022. 06. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-transactions-per-visit/"> 1336. Number of Transactions per Visit </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1336.sql"> 1336.sql </a> </td>
    <td> 2022. 06. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sales-by-day-of-the-week/"> 1479. Sales by Day of the Week </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1479.sql"> 1479.sql </a> </td>
    <td> 2022. 06. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/hopper-company-queries-i/"> 1635. Hopper Company Queries I </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1635.sql"> 1635.sql </a> </td>
    <td> 2022. 06. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/hopper-company-queries-ii/"> 1645. Hopper Company Queries II </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1645.sql"> 1645.sql </a> </td>
    <td> 2022. 06. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/hopper-company-queries-iii/"> 1651. Hopper Company Queries III </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1651.sql"> 1651.sql </a> </td>
    <td> 2022. 06. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/page-recommendations-ii/"> 1892. Page Recommendations II </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1892.sql"> 1892.sql </a> </td>
    <td> 2022. 06. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/leetcodify-friends-recommendations/"> 1917. Leetcodify Friends Recommendations </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1917.sql"> 1917.sql </a> </td>
    <td> 2022. 06. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/leetcodify-similar-friends/"> 1919. Leetcodify Similar Friends </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/1919.sql"> 1919.sql </a> </td>
    <td> 2022. 06. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/"> 2004. The Number of Seniors and Juniors to Join the Company </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2004.sql"> 2004.sql </a> </td>
    <td> 2022. 06. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/longest-winning-streak/"> 2173. Longest Winning Streak </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2173.sql"> 2173.sql </a> </td>
    <td> 2022. 06. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/finding-the-topic-of-each-post/"> 2199. Finding the Topic of Each Post </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2199.sql"> 2199.sql </a> </td>
    <td> 2022. 06. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/"> 2153. The Number of Passengers in Each Bus II </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2153.sql"> 2153.sql </a> </td>
    <td> 2022. 06. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/build-the-equation/"> 2118. Build the Equation </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2118.sql"> 2118.sql </a> </td>
    <td> 2022. 06. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/dynamic-pivoting-of-a-table/"> 2252. Dynamic Pivoting of a Table </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2252.sql"> 2252.sql </a> </td>
    <td> 2022. 07. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/dynamic-unpivoting-of-a-table/"> 2253. Dynamic Unpivoting of a Table </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2253.sql"> 2253.sql </a> </td>
    <td> 2022. 07. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/generate-the-invoice/"> 2362. Generate the Invoice </a> </td>
    <td> <a href="./LeetCode/SQL/3_Hard/2362.sql"> 2362.sql </a> </td>
    <td> 2022. 08. 06 </td>
</tr>
</table>

</details>

#### Python

<details>

<summary> Easy </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/"> 1523. Count Odd Numbers in an Interval Range </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1523.py"> 1523.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/"> 1491. Average Salary Excluding the Minimum and Maximum Salary </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1491.py"> 1491.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/binary-search/"> 704. Binary Search </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/704.py"> 704.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/first-bad-version/"> 278. First Bad Version </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/278.py"> 278.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/search-insert-position/"> 35. Search Insert Position </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/35.py"> 35.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/"> 1281. Subtract the Product and Sum of Digits of an Integer </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1281.py"> 1281.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-1-bits/"> 191. Number of 1 Bits </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/191.py"> 191.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/two-sum/"> 1. Two Sum </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1.py"> 1.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/check-if-it-is-a-straight-line/"> 1232. Check If It Is a Straight Line </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1232.py"> 1232.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/concatenation-of-array/"> 1929. Concatenation of Array </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1929.py"> 1929.py </a></td>
    <td> </td>
    <td> 2022. 08. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/to-lower-case/"> 709. To Lower Case </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/709.py"> 709.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/goal-parser-interpretation/"> 1678. Goal Parser Interpretation </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1678.py"> 1678.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/roman-to-integer/"> 13. Roman to Integer </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/13.py"> 13.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/first-unique-character-in-a-string/"> 387. First Unique Character in a String </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/387.py"> 387.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/first-letter-to-appear-twice/"> 2351. First Letter to Appear Twice </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/2351.py"> 2351.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/two-sum-iii-data-structure-design/"> 170. Two Sum III - Data structure design </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/170.py"> 170.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/unique-morse-code-words/"> 804. Unique Morse Code Words </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/804.py"> 804.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/valid-anagram/"> 242. Valid Anagram </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/242.py"> 242.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/valid-anagram/"> 217. Contains Duplicate </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/217.py"> 217.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/contains-duplicate-ii/"> 219. Contains Duplicate II </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/219.py"> 219.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/"> 1779. Find Nearest Point That Has the Same X or Y Coordinate </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1779.py"> 1779.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/largest-perimeter-triangle/"> 976. Largest Perimeter Triangle </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/976.py"> 976.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/"> 1309. Decrypt String from Alphabet to Integer Mapping </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1309.py"> 1309.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/verifying-an-alien-dictionary/"> 953. Verifying an Alien Dictionary </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/953.py"> 953.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/power-of-four/"> 342. Power of Four </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/342.py"> 342.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/power-of-three/"> 326. Power of Three </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/326.py"> 326.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/ransom-note/"> 383. Ransom Note </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/383.py"> 383.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-the-difference/"> 389. Find the Difference </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/389.py"> 389.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/merge-strings-alternately/"> 1768. Merge Strings Alternately </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1768.py"> 1768.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/n-th-tribonacci-number/"> 1137. N-th Tribonacci Number </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1137.py"> 1137.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/implement-queue-using-stacks/"> 232. Implement Queue using Stacks </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/232.py"> 232.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/design-parking-system/"> 1603. Design Parking System </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1603.py"> 1603.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/"> 1356. Sort Integers by The Number of 1 Bits </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1356.py"> 1356.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/"> 1886. Determine Whether Matrix Can Be Obtained By Rotation </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1886.py"> 1886.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 08. 31 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sign-of-the-product-of-an-array/"> 1822. Sign of the Product of an Array </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1822.py"> 1822.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/"> 1502. Can Make Arithmetic Progression From Sequence </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1502.py"> 1502.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/"> 1790. Check if One String Swap Can Make Strings Equal </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1790.py"> 1790.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/average-of-levels-in-binary-tree/"> 637. Average of Levels in Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/637.py"> 637.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/binary-tree-postorder-traversal/"> 145. Binary Tree Postorder Traversal </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/145.py"> 145.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/binary-tree-postorder-traversal/"> 94. Binary Tree Inorder Traversal </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/94.py"> 94.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/"> 144. Binary Tree Preorder Traversal </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/144.py"> 144.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/"> 104. Maximum Depth of Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/104.py"> 104.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/check-if-an-array-is-consecutive/"> 2229. Check if an Array Is Consecutive </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/2229.py"> 2229.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/construct-string-from-binary-tree/"> 606. Construct String from Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/606.py"> 606.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sum-of-left-leaves/"> 404. Sum of Left Leaves </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/404.py"> 404.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"> 121. Best Time to Buy and Sell Stock </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/121.py"> 121.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-difference-between-increasing-elements/"> 2016. Maximum Difference Between Increasing Elements </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/2016.py"> 2016.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/two-furthest-houses-with-different-colors/"> 2078. Two Furthest Houses With Different Colors </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/2078.py"> 2078.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/power-of-two/"> 231. Power of Two </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/231.py"> 231.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/single-number/"> 136. Single Number </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/136.py"> 136.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/missing-number/"> 268. Missing Number </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/268.py"> 268.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reverse-words-in-a-string-iii/"> 557. Reverse Words in a String III </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/557.py"> 557.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reverse-string/"> 344. Reverse String </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/344.py"> 344.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reverse-string/"> 1119. Remove Vowels from a String </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1119.py"> 1119.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reverse-string-ii/"> 541. Reverse String II </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/541.py"> 541.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reverse-vowels-of-a-string/"> 345. Reverse Vowels of a String </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/345.py"> 345.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/second-largest-digit-in-a-string/"> 1796. Second Largest Digit in a String </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1796.py"> 1796.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/"> 2259. Remove Digit From Number to Maximize Result </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/2259.py"> 2259.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/path-sum/"> 112. Path Sum </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/112.py"> 112.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/guess-number-higher-or-lower/"> 374. Guess Number Higher or Lower </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/374.py"> 374.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/valid-perfect-square/"> 367. Valid Perfect Square </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/367.py"> 367.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sqrtx/"> 69. Sqrt(x) </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/69.py"> 69.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-smallest-letter-greater-than-target/"> 744. Find Smallest Letter Greater Than Target </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/744.py"> 744.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 09. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/arranging-coins/"> 441. Arranging Coins </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/441.py"> 441.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/kth-missing-positive-number/"> 1539. Kth Missing Positive Number </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1539.py"> 1539.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/"> 1608. Special Array With X Elements Greater Than or Equal X </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1608.py"> 1608.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/"> 1351. Count Negative Numbers in a Sorted Matrix </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1351.py"> 1351.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/"> 1337. The K Weakest Rows in a Matrix </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1337.py"> 1337.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/check-if-n-and-its-double-exist/"> 1346. Check If N and Its Double Exist </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1346.py"> 1346.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/"> 350. Intersection of Two Arrays II </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/350.py"> 350.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/intersection-of-two-arrays/"> 349. Intersection of Two Arrays </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/349.py"> 349.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-the-distance-value-between-two-arrays/"> 1385. Find the Distance Value Between Two Arrays </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1385.py"> 1385.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/merge-sorted-array/"> 88. Merge Sorted Array </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/88.py"> 88.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/pascals-triangle/"> 118. Pascal's Triangle </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/118.py"> 118.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/pascals-triangle-ii/"> 119. Pascal's Triangle II  </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/119.py"> 119.py </a></td>
    <td> <a href=""> </a> </td>
    <td> 2022. 10. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/determine-if-string-halves-are-alike/description/"> 1704. Determine if String Halves Are Alike </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1704.py"> 1704.py </a></td>
    <td> <a href="">  </a> </td>
    <td> 2022. 12. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/middle-of-the-linked-list/description/"> 876. Middle of the Linked List </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/876.py"> 876.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/single-row-keyboard/description/"> 1165. Single-Row Keyboard </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1165.py"> 1165.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/jewels-and-stones/description/"> 771. Jewels and Stones </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/771.py"> 771.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/search-in-a-binary-search-tree/description/"> 700. Search in a Binary Search Tree </a> </td>
    <td> <a href="./LeetCode/Python/1_Easy/700.py"> 700.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/range-sum-of-bst/description/"> 938. Range Sum of BST </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/938.py"> 938.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/leaf-similar-trees/description/"> 872. Leaf-Similar Trees </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/872.py"> 872.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/climbing-stairs/description/"> 70. Climbing Stairs </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/70.py"> 70.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-if-path-exists-in-graph/description/"> 1971. Find if Path Exists in Graph </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1971.py"> 1971.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/running-sum-of-1d-array/description/"> 1480. Running Sum of 1d Array </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1480.py"> 1480.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/richest-customer-wealth/description/"> 1672. Richest Customer Wealth </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1672.py"> 1672.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/fizz-buzz/description/"> 412. Fizz Buzz </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/412.py"> 412.py </a> </td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/word-pattern/description/"> 290. Word Pattern </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/290.py"> 290.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/confusing-number/description/"> 1056. Confusing Number </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1056.py"> 1056.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/isomorphic-strings/description/"> 205. Isomorphic Strings </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/205.py"> 205.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/detect-capital/description/"> 520. Detect Capital </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/520.py"> 520.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/delete-columns-to-make-sorted/description/"> 944. Delete Columns to Make Sorted </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/944.py"> 944.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/"> 1342. Number of Steps to Reduce a Number to Zero </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/1342.py"> 1342.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/same-tree/description/"> 100. Same Tree </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/100.py"> 100.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/cousins-in-binary-tree/description/"> 993. Cousins in Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/1_Easy/993.py"> 993.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 11 </td>
</tr>
</table>

</details>

<details>

<summary> Medium </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"> 167. Two Sum II - Input Array Is Sorted </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/167.py"> 167.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reduce-array-size-to-the-half/solution/"> 1338. Reduce Array Size to The Half </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1338.py"> 1338.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reordered-power-of-2/"> 869. Reordered Power of 2 </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/869.py"> 869.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-islands/"> 200. Number of Islands </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/200.py"> 200.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/rotate-image/"> 48. Rotate Image </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/48.py"> 48.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 08. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/count-good-nodes-in-binary-tree/"> 1448. Count Good Nodes in Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1448.py"> 1448.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/numbers-with-same-consecutive-differences/"> 967. Numbers With Same Consecutive Differences </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/967.py"> 967.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/binary-tree-pruning/"> 814. Binary Tree Pruning </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/814.py"> 814.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/"> 298. Binary Tree Longest Consecutive Sequence </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/298.py"> 298.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/design-hit-counter/"> 362. Design Hit Counter </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/362.py"> 362.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/"> 1996. The Number of Weak Characters in the Game </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1996.py"> 1996.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-subarray/"> 53. Maximum Subarray </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/53.py"> 53.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/bag-of-tokens/"> 948. Bag of Tokens </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/948.py"> 948.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-product-subarray/"> 152. Maximum Product Subarray </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/152.py"> 152.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii"> 122. Best Time to Buy and Sell Stock II </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/122.py"> 122.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/utf-8-validation"> 393. UTF-8 Validation </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/393.py"> 393.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/"> 1457. Pseudo-Palindromic Paths in a Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1457.py"> 1457.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 09. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-original-array-from-doubled-array/"> 2007. Find Original Array From Doubled Array </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/2007.py"> 2007.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/path-sum-ii/"> 113. Path Sum II </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/113.py"> 113.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/peak-index-in-a-mountain-array/"> 852. Peak Index in a Mountain Array </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/852.py"> 852.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 09. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"> 34. Find First and Last Position of Element in Sorted Array </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/34.py"> 34.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 10. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/search-a-2d-matrix/"> 74. Search a 2D Matrix </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/74.py"> 74.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 10. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sum-of-square-numbers/"> 633. Sum of Square Numbers </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/633.py"> 633.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 10. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/"> 1855. Maximum Distance Between a Pair of Values </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1855.py"> 1855.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 10. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"> 153. Find Minimum in Rotated Sorted Array </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/153.py"> 153.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 10. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/"> 33. Search in Rotated Sorted Array </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/33.py"> 33.py </a></td>
    <td> <a href="">  </a></td>
    <td> 2022. 10. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/find-triangular-sum-of-an-array/"> 2221. Find Triangular Sum of an Array </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/2221.py"> 2221.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 10. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/determine-if-two-strings-are-close/description/"> 1657. Determine if Two Strings Are Close </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1657.py"> 1657.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/sort-characters-by-frequency/description/"> 451. Sort Characters By Frequency </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/451.py"> 451.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/minimum-average-difference/description/"> 2256. Minimum Average Difference </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/2256.py"> 2256.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/odd-even-linked-list/description/"> 328. Odd Even Linked List </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/328.py"> 328.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/"> 1339. Maximum Product of Splitted Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1339.py"> 1339.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/description/"> 150. Evaluate Reverse Polish Notation </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/150.py"> 150.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reverse-words-in-a-string/description/"> 151. Reverse Words in a String </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/151.py"> 151.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/reverse-words-in-a-string-ii/description/"> 186. Reverse Words in a String II </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/186.py"> 186.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/daily-temperatures/description/"> 739. Daily Temperatures </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/739.py"> 739.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/keys-and-rooms/description/"> 841. Keys and Rooms </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/841.py"> 841.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/"> 323. Number of Connected Components in an Undirected Graph </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/323.py"> 323.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/number-of-provinces/description/"> 547. Number of Provinces </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/547.py"> 547.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/"> 1167. Minimum Cost to Connect Sticks </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1167.py"> 1167.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 12. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/"> 2244. Minimum Rounds to Complete All Tasks </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/2244.py"> 2244.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/"> 452. Minimum Number of Arrows to Burst Balloons </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/452.py"> 452.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/maximum-ice-cream-bars/description/"> 1833. Maximum Ice Cream Bars </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1833.py"> 1833.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/gas-station/description/"> 134. Gas Station </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/134.py"> 134.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/minimum-health-to-beat-game/description/"> 2214. Minimum Health to Beat Game </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/2214.py"> 2214.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/"> 255. Verify Preorder Sequence in Binary Search Tree </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/255.py"> 255.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/"> 1061. Lexicographically Smallest Equivalent String </a></td>
    <td> <a href="./LeetCode/Python/2_Medium/1061.py"> 1061.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 15 </td>
</tr>
</table>

</details>

<details>

<summary> Hard </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/"> 987. Vertical Order Traversal of a Binary Tree </a></td>
    <td> <a href="./LeetCode/Python/3_Hard/987"> 987.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2022. 09. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://leetcode.com/problems/max-points-on-a-line/description/"> 149. Max Points on a Line </a></td>
    <td> <a href="./LeetCode/Python/3_Hard/149"> 149.py </a></td>
    <td> <a href=""> </a></td>
    <td> 2023. 01. 09 </td>
</tr>
</table>

</details>

### Baekjoon

#### C

<details>

<summary> Bronze </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 분류 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2739"> 2739번: 구구단 </a> </td>
    <td> 수학, 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2739.c"> 2739.c </a> </td>
    <td> 2022. 10. 31 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10951"> 10951번: A+B - 4 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10951.c"> 10951.c </a> </td>
    <td> 2022. 11. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2438"> 2438번: 별 찍기 - 1 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2438.c"> 2438.c </a> </td>
    <td> 2022. 11. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11654"> 11654번: 아스키 코드 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/11654.c"> 11654.c </a> </td>
    <td> 2022. 11. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2744"> 2744번: 대소문자 바꾸기 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2744.c"> 2744.c </a> </td>
    <td> 2022. 11. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2743"> 2743번: 단어 길이 재기 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2743.c"> 2743.c </a> </td>
    <td> 2022. 11. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2754"> 2754번: 학점계산 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2754.c"> 2754.c </a> </td>
    <td> 2022. 11. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2755"> 2755번: 이번학기 평점은 몇점? </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2755.c"> 2755.c </a> </td>
    <td> 2022. 11. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11718"> 11718번: 그대로 출력하기 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/11718.c"> 11718.c </a> </td>
    <td> 2022. 11. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/9086"> 9086번: 문자열 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/9086.c"> 9086.c </a> </td>
    <td> 2022. 11. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10809"> 10809번: 알파벳 찾기 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10809.c"> 10809.c </a> </td>
    <td> 2022. 11. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2475"> 2475번: 검증수 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2475.c"> 2475.c </a> </td>
    <td> 2022. 11. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2439"> 2439번: 별 찍기 - 2 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2439.c"> 2439.c </a> </td>
    <td> 2022. 11. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2742"> 2742번: 기찍 N </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2742.c"> 2742.c </a> </td>
    <td> 2022. 11. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1085"> 1085번: 직사각형에서 탈출 </a> </td>
    <td> 수학, 기하학 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/1085.c"> 1085.c </a> </td>
    <td> 2022. 11. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/4153"> 4153번: 직각삼각형 </a> </td>
    <td> 수학, 기하학, 피타고라스 정리 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/4153.c"> 4153.c </a> </td>
    <td> 2022. 11. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/4153"> 15964번: 이상한 기호 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/15964.c"> 15964.c </a> </td>
    <td> 2022. 11. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/15829"> 15829번: Hashing </a> </td>
    <td> 문자열, 해싱 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/15829.c"> 15829.c </a> </td>
    <td> 2022. 11. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10250"> 10250번: ACM 호텔 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10250.c"> 10250.c </a> </td>
    <td> 2022. 11. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1259"> 1259번: 팰린드롬수 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/1259.c"> 1259.c </a> </td>
    <td> 2022. 11. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2609"> 2609번: 최대공약수와 최소공배수 </a> </td>
    <td> 수학, 정수론, 유클리드 호제법 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2609.c"> 2609.c </a> </td>
    <td> 2022. 11. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11050"> 11050번: 이항 계수 1 </a> </td>
    <td> 수학, 구현, 조합론 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/11050.c"> 11050.c </a> </td>
    <td> 2022. 11. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2869"> 2869번: 달팽이는 올라가고 싶다 </a> </td>
    <td> 수학 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2869.c"> 2869.c </a> </td>
    <td> 2022. 11. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2386"> 2386번: 도비의 영어 공부 </a> </td>
    <td> 구현, 문자열, 브루트포스 알고리즘 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2386.c"> 2386.c </a> </td>
    <td> 2022. 11. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10989"> 10989번: 수 정렬하기 3 </a> </td>
    <td> 정렬 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10989.c"> 10989.c </a> </td>
    <td> 2022. 11. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2558"> 2558번: A+B - 2 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2558.c"> 2558.c </a> </td>
    <td> 2022. 11. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10718"> 10718번: We love kriii </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10718.c"> 10718.c </a> </td>
    <td> 2022. 11. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/8393"> 8393번: 합 </a> </td>
    <td> 수학, 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/8393.c"> 8393.c </a> </td>
    <td> 2022. 11. 23 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/4101"> 4101번: 크냐? </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/4101.c"> 4101.c </a> </td>
    <td> 2022. 11. 24 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/4999"> 4999번: 아! </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/4999.c"> 4999.c </a> </td>
    <td> 2022. 11. 25 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11021"> 11021번: A+B - 7 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/11021.c"> 11021.c </a> </td>
    <td> 2022. 11. 26 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10926"> 10926번: ??! </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10926.c"> 10926.c </a> </td>
    <td> 2022. 11. 27 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11942"> 11942번: 고려대는 사랑입니다. </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/11942.c"> 11942.c </a> </td>
    <td> 2022. 11. 28 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/16394"> 16394번: 홍익대학교 </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/16394.c"> 16394.c </a> </td>
    <td> 2022. 11. 29 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/16170"> 16170번: 오늘의 날짜는? </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/16170.c"> 16170.c </a> </td>
    <td> 2022. 11. 30 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/18108"> 18108번: 1998년생인 내가 태국에서는 2541년생?! </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/18108.c"> 18018.c </a> </td>
    <td> 2022. 12. 01 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/25311"> 25311번: UCPC에서 가장 쉬운 문제 번호는? </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/25311.c"> 25311.c </a> </td>
    <td> 2022. 12. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/17256"> 17256번: 달달함이 넘쳐흘러 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/17256.c"> 17256.c </a> </td>
    <td> 2022. 12. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/15733"> 15733번: 나는 누구인가 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/15733.c"> 15733.c </a> </td>
    <td> 2022. 12. 04 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/15962"> 15962번: 새로운 시작 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/15962.c"> 15962.c </a> </td>
    <td> 2022. 12. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/16430"> 16430번: 제리와 톰 </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/16430.c"> 16430.c </a> </td>
    <td> 2022. 12. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/20492"> 20492번: 세금 </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/20492.c"> 20492.c </a> </td>
    <td> 2022. 12. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/25372"> 25372번: 성택이의 은밀한 비밀번호 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/25372.c"> 25372.c </a> </td>
    <td> 2022. 12. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/26082"> 26082번: WARBOY </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/26082.c"> 26082.c </a> </td>
    <td> 2022. 12. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2440"> 2440번: 별 찍기 - 3 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2440.c"> 2440.c </a> </td>
    <td> 2022. 12. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10808"> 10808번: 알파벳 개수 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10808.c"> 10808.c </a> </td>
    <td> 2022. 12. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11365"> 11365번: !밀비 급일 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/11365.c"> 11365.c </a> </td>
    <td> 2022. 12. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2083"> 2083번: 럭비 클럽 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2083.c"> 2083.c </a> </td>
    <td> 2022. 12. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2480"> 2480번: 주사위 세 개 </a> </td>
    <td> 수학, 사칙연산, 많은 조건 분기 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/2480.c"> 2480.c </a> </td>
    <td> 2022. 12. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/3046"> 3046번: R2 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/3046.c"> 3046.c </a> </td>
    <td> 2022. 12. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2845"> 2845번: 파티가 끝나고 난 뒤 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/3046.c"> 2845.c </a> </td>
    <td> 2022. 12. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/3003"> 3003번: 킹, 퀸, 룩, 비숍, 나이트, 폰 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/3003.c"> 3003.c </a> </td>
    <td> 2022. 12. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/5522"> 5522번: 카드 게임 </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/5522.c"> 5522.c </a> </td>
    <td> 2022. 12. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10430"> 10430번: 나머지 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/10430.c"> 10430.c </a> </td>
    <td> 2022. 12. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/15727"> 15727번: 조별과제를 하려는데 조장이 사라졌다 </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/15727.c"> 15727.c </a> </td>
    <td> 2022. 12. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/17295"> 17295번: 엔드게임 스포일러 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/C/01_Bronze/17295.c"> 17295.c </a> </td>
    <td> 2022. 12. 22 </td>
</tr>
</table>

</details>

<details>

<summary> Silver </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 분류 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1978"> 1978번: 소수 찾기 </a> </td>
    <td> 수학, 정수론, 소수 판정, 에라토스테네스의 체 </td>
    <td> <a href="./Baekjoon/C/02_Silver/1978.c"> 1978.c </a> </td>
    <td> 2022. 11. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1929"> 1929번: 소수 구하기 </a> </td>
    <td> 수학, 정수론, 소수 판정, 에라토스테네스의 체 </td>
    <td> <a href="./Baekjoon/C/02_Silver/1929.c"> 1929.c </a> </td>
    <td> 2022. 11. 20 </td>
</tr>

</table>

</details>

#### Python

<details>

<summary> Bronze </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 분류 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/18406"> 18406번: 럭키 스트레이트 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/18406.py"> 18406.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-18406"> [ 알고리즘 ] 백준 18406번: 럭키 스트레이트 </a> </td>
    <td> 2022. 07. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2557"> 2557번: Hello World </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2557.py"> 2557.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10699"> 10699번: 오늘 날짜 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10699.py"> 10699.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/7287"> 7287번: 등록 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/7287.py"> 7287.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10171"> 10171번: 고양이 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10171.py"> 10171.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10172"> 10172번: 개 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10172.py"> 10172.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/25083"> 25083번: 새싹 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/25083.py"> 25083.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1000"> 1000번: A+B </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/1000.py"> 1000.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1001"> 1001번: A-B </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/1001.py"> 1001.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10998"> 10998번: AxB </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10998.py"> 10998.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10869"> 10869번: 사칙연산 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10869.py"> 10869.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1008"> 1008번: A/B </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/1008.py"> 1008.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11382"> 11382번: 꼬마 정민 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/11382.py"> 11382.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1330"> 1330번: 두 수 비교하기 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/1330.py"> 1330.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/9498"> 9498번: 시험 성적 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/9498.py"> 9498.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/14681"> 14681번: 사분면 고르기 </a> </td>
    <td> 구현, 기하학 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/14681.py"> 14681.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2420"> 2420번: 사파리월드 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2420.py"> 2420.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2753"> 2753번: 윤년 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2753.py"> 2753.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/15552"> 15552번: 빠른 A+B </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/15552.py"> 15552.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10871"> 10871번: X보다 작은 수 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10871.py"> 10871.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10807"> 10807번: 개수 세기 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10807.py"> 10807.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/5597"> 5597번: 과제 안 내신 분..? </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/5597.py"> 5597.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2738"> 2738번: 행렬 덧셈 </a> </td>
    <td> 수학, 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2738.py"> 2738.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 19 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2741"> 2741번: N 찍기 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2741.py"> 2741.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 20 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10950"> 10950번: A+B - 3 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10950.py"> 10950.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10872"> 10872번: 팩토리얼 </a> </td>
    <td> 수학, 구현, 조합론 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10872.py"> 10872.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 21 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10952"> 10952번: A+B - 5 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10952.py"> 10952.py </a> </td>
    <td>  </td>
    <td> 2022. 07. 22 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2750"> 2750번: 수 정렬하기 </a> </td>
    <td> 구현, 정렬 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2750"> 2750.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1546"> 1546번: 평균 </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/1546.py"> 1546.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1157"> 1157번: 단어 공부 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/1157.py"> 1157.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1152"> 1152번: 단어의 개수 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/1152.py"> 1152.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2577"> 2577번: 숫자의 개수 </a> </td>
    <td> 수학, 구현, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2557.py"> 2577.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2908"> 2908번: 상수 </a> </td>
    <td> 수학, 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2908.py"> 2908.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/3052"> 3052번: 나머지 </a> </td>
    <td> 수학, 사칙연산 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/3052.py"> 3052.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/8958"> 8958번: OX퀴즈 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/8958.py"> 8958.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2675"> 2675번: 문자열 제출 </a> </td>
    <td> 구현, 문자열 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2675.py"> 2675.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2920"> 2920번: 음계 </a> </td>
    <td> 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/2920.py"> 2920.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10818"> 10818번: 최소, 최대 </a> </td>
    <td> 수학, 구현 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/10818.py"> 10818.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11720"> 11720번: 숫자의 합 </a> </td>
    <td> 수학, 구현, 문자열 </td>
    <td> <a href="./Baekjoon/Python/01_Bronze/11720.py"> 11720.py </a> </td>
    <td>  </td>
    <td> 2022. 08. 22 </td>
</tr>
</table>

</details>

<details>

<summary> Silver </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 분류 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11399"> 11399번: ATM </a> </td>
    <td> 그리디 알고리즘, 정렬 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/11399.py"> 11399.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-11399-ATM"> [ 알고리즘 ] 백준 11399번: ATM </a> </td>
    <td> 2022. 06. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1439"> 1439번: 뒤집기 </a> </td>
    <td> 문자열, 그리디 알고리즘 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/1439.py"> 1439.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1439"> [ 알고리즘 ] 백준 1439번: 뒤집기 </a> </td>
    <td> 2022. 06. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1026"> 1026번: 보물 </a> </td>
    <td> 수학, 그리디 알고리즘, 정렬 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/1026.py"> 1026.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1026"> [ 알고리즘 ] 백준 1026번: 보물 </a> </td>
    <td> 2022. 06. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2217"> 2217번: 로프 </a> </td>
    <td> 수학, 그리디 알고리즘, 정렬 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/2217.py"> 2217.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-2217"> [ 알고리즘 ] 백준 2217번: 로프 </a> </td>
    <td> 2022. 06. 15 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/28397"> 2839번: 설탕 배달 </a> </td>
    <td> 수학, 다이나믹 프로그래밍, 그리디 알고리즘 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/2839.py"> 2839.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-2839"> [ 알고리즘 ] 백준 2839번: 설탕 배달 </a> </td>
    <td> 2022. 06. 16 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11047"> 11047번: 동전 0 </a> </td>
    <td> 그리디 알고리즘 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/11047.py"> 11047.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-11047"> [ 알고리즘 ] 백준 11047번: 동전 0 </a> </td>
    <td> 2022. 06. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/4673"> 4673번: 셀프 넘버 </a> </td>
    <td> 수학, 구현, 브루트포스 알고리즘 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/4673.py"> 4673.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-4673"> [ 알고리즘 ] 백준 4673번: 셀프 넘버 </a> </td>
    <td> 2022. 06. 17 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/4673"> 10773번: 제로 </a> </td>
    <td> 구현, 자료 구조, 스택 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/10773.py"> 10773.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-10773"> [ 알고리즘 ] 백준 10773번: 제로 </a> </td>
    <td> 2022. 06. 18 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1541"> 1541번: 잃어버린 괄호 </a> </td>
    <td> 수학, 문자열, 그리디 알고리즘, 문자열 파싱 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/1541.py"> 1541.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1541"> [ 알고리즘 ] 백준 1541번: 잃어버린 괄호 </a> </td>
    <td> 2022. 07. 05 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1946"> 1946번: 신입 사원 </a> </td>
    <td> 그리디 알고리즘, 정렬 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/1946.py"> 1946.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1946"> [ 알고리즘 ] 백준 1946번: 신입 사원 </a> </td>
    <td> 2022. 07. 06 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1213"> 1213번: 팰린드롬 만들기 </a> </td>
    <td> 구현, 문자열, 그리디 알고리즘, 정렬 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/1213.py"> 1213.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1213"> [ 알고리즘 ] 백준 1213번: 팰린드롬 만들기 </a> </td>
    <td> 2022. 07. 08 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/18111"> 18111번: 마인크래프트 </a> </td>
    <td> 구현, 브루트포스 알고리즘 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/18111.py"> 18111.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-18111"> [ 알고리즘 ] 백준 18111번: 마인크래프트 </a> </td>
    <td> 2022. 07. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1931"> 1931번: 회의실 배정 </a> </td>
    <td> 그리디 알고리즘, 정렬 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/1931.py"> 1931.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1931"> [ 알고리즘 ] 백준 1931번: 회의실 배정 </a> </td>
    <td> 2022. 07. 12 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/10815"> 10815번: 숫자 카드 </a> </td>
    <td> 자료 구조, 정렬, 이분 탐색 </td>
    <td> <a href="./Baekjoon/Python/02_Silver/10815.py"> 10815.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-10815"> [ 알고리즘 ] 백준 10815번: 숫자 카드 </a> </td>
    <td> 2022. 07. 31 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2805"> 2805번: 나무 자르기 </a> </td>
    <td> 이분 탐색, 매개 변수 탐색 </td>
    <td> <a href="/Baekjoon/Python/02_Silver/2805.py"> 2805.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-2805"> [ 알고리즘 ] 백준 2805번: 나무 자르기 </a> </td>
    <td> 2022. 08. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1654"> 1654번: 랜선 자르기 </a> </td>
    <td> 이분 탐색, 매개 변수 탐색 </td>
    <td> <a href="/Baekjoon/Python/02_Silver/1654.py"> 1654.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1654"> [ 알고리즘 ] 백준 1654번: 랜선 자르기 </a> </td>
    <td> 2022. 08. 09 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1966"> 1966번: 프린터 큐 </a> </td>
    <td> 구현, 자료 구조, 시뮬레이션, 큐 </td>
    <td> <a href="/Baekjoon/Python/02_Silver/1966.py"> 1966.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1966"> [ 알고리즘 ] 백준 1966번: 프린터 큐 </a> </td>
    <td> 2022. 08. 10 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2504"> 2504번: 괄호의 값 </a> </td>
    <td> 구현, 자료 구조, 스택, 재귀 </td>
    <td> <a href="/Baekjoon/Python/02_Silver/2504.py"> 2504.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-2504"> [ 알고리즘 ] 백준 2504번: 괄호의 값 </a> </td>
    <td> 2022. 08. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11659"> 11659번: 구간 합 구하기 4 </a> </td>
    <td> 구현, 자료 구조, 스택, 재귀 </td>
    <td> <a href="/Baekjoon/Python/02_Silver/11659.py"> 11659.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-11659"> [ 알고리즘 ] 백준 11659번: 구간 합 구하기 4 </a> </td>
    <td> 2022. 08. 13 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/11660"> 11660번: 구간 합 구하기 5 </a> </td>
    <td> 다이나믹 프로그래밍, 누적 합 </td>
    <td> <a href="/Baekjoon/Python/02_Silver/11660.py"> 11660.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-11660"> [ 알고리즘 ] 백준 11660번: 구간 합 구하기 5 </a> </td>
    <td> 2022. 08. 14 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1874"> 1874번: 스택 수열 </a> </td>
    <td> 자료 구조, 스택 </td>
    <td> <a href="/Baekjoon/Python/02_Silver/1874.py"> 1874.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1874"> [ 알고리즘 ] 백준 1874번: 스택 수열 </a> </td>
    <td> 2022. 08. 15 </td>
</tr>
</table>

</details>

<details>

<summary> Gold </summary>

<table>
<tr>
    <th> 문제 </th>
    <th> 분류 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/3190"> 3190번: 뱀 </a> </td>
    <td> 구현, 자료 구조, 시뮬레이션, 덱, 큐 </td>
    <td> <a href="./Baekjoon/Python/03_Gold/3190.py"> 3190.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-3190"> [ 알고리즘 ] 백준 3190번: 뱀 </a> </td>
    <td> 2022. 07. 02 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/15686"> 15686번: 치킨 배달 </a> </td>
    <td> 구현, 브루트포스 알고리즘, 백트래킹 </td>
    <td> <a href="./Baekjoon/Python/03_Gold/15686.py"> 15686.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-15686"> [ 알고리즘 ] 백준 15686번: 치킨 배달 </a> </td>
    <td> 2022. 07. 03 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1339"> 1339번: 단어 수학 </a> </td>
    <td> 그리디 알고리즘, 브루트포스 알고리즘 </td>
    <td> <a href="./Baekjoon/Python/03_Gold/1339.py"> 1339.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1339"> [ 알고리즘 ] 백준 1339번: 단어 수학 </a> </td>
    <td> 2022. 07. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1092"> 1092번: 배 </a> </td>
    <td> 그리디 알고리즘, 정렬 </td>
    <td> <a href="./Baekjoon/Python/03_Gold/1092.py"> 1092.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-1092"> [ 알고리즘 ] 백준 1092번: 배 </a> </td>
    <td> 2022. 08. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2470"> 2470번: 두 용액 </a> </td>
    <td> 정렬, 이분 탐색, 두 포인터 </td>
    <td> <a href="./Baekjoon/Python/03_Gold/2470.py"> 2470.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-2470"> [ 알고리즘 ] 백준 2470번: 두 용액 </a> </td>
    <td> 2022. 08. 07 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/2110"> 2110번: 공유기 설치 </a> </td>
    <td> 이분 탐색, 매개 변수 탐색 </td>
    <td> <a href="./Baekjoon/Python/03_Gold/2110.py"> 2110.py </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-baekjoon-2110"> [ 알고리즘 ] 백준 2110번: 공유기 설치 </a> </td>
    <td> 2022. 08. 11 </td>
</tr>
<tr align="left">
    <td> <a href="https://www.acmicpc.net/problem/1918"> 1918번: 후위 표기식 </a> </td>
    <td> 자료 구조, 스택 </td>
    <td> <a href="./Baekjoon/Python/03_Gold/1918.py"> 1918.py </a> </td>
    <td> <a href=""> [ 알고리즘 ] 백준 1918번: 후위 표기식 </a> </td>
    <td> 2022. 10. 29 </td>
</tr>
</table>

</details>

### 이것이 취업을 위한 코딩 테스트다 with 파이썬

<details>

<summary> Source Code </summary>

<table>
<tr>
    <th> 알고리즘 </th>
    <th> 분류 </th>
    <th> 코드 </th>
    <th> 풀이 </th>
    <th> 일자 </th>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 실전문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/01_실전문제/01.py"> 큰 수의 법칙 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 24 </td>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 실전문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/01_실전문제/02.py"> 숫자 카드 게임 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 24 </td>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 실전문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/01_실전문제/03.py"> 1이 될 때까지 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 24 </td>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/02_기출문제/01.py"> 모험가 길드 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 24 </td>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/02_기출문제/02.py"> 곱하기 혹은 더하기 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 24 </td>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/02_기출문제/03.py"> 문자열 뒤집기 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 24 </td>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/02_기출문제/04.py"> 만들 수 없는 금액 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 24 </td>
</tr>
<tr align="left">
    <td> 그리디 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/01_Greedy/02_기출문제/05.py"> 볼링공 고르기 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디 </a> </td>
    <td> 2022. 06. 26 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 실전문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/01_실전문제/01.py"> 왕실의 나이트 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 06. 28 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 실전문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/01_실전문제/02.py"> 게임 개발 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 06. 29 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/02_기출문제/01.py"> 럭키 스트레이트 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 06. 30 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/02_기출문제/02.py"> 문자열 재정렬 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 06. 30 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/02_기출문제/03.py"> 문자열 압축 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 06. 30 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/02_기출문제/04.py"> 자물쇠와 열쇠 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 07. 03 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/02_기출문제/05.py"> 뱀 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 07. 03 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/02_기출문제/06.py"> 기둥과 보 설치 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 07. 03 </td>
</tr>
<tr align="left">
    <td> 구현 </td>
    <td> 기출문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/02_Implementation/02_기출문제/07.py"> 치킨 배달 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현 </a> </td>
    <td> 2022. 07. 03 </td>
</tr>
<tr align="left">
    <td> DFS/BFS </td>
    <td> 실전문제 </td>
    <td> <a href="./이것이 취업을 위한 코딩 테스트다/03_DFS&BFS/01_실전문제/01.py"> 음료수 얼려 먹기 </a> </td>
    <td> <a href="https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-dfs-and-bfs"> [ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : DFS/BFS </a> </td>
    <td> 2022. 07. 10 </td>
</tr>
</table>

</details>
