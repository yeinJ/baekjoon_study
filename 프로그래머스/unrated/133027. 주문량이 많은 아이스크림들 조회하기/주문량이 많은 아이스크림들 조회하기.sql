-- 코드를 입력하세요
-- 7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL문 작성

SELECT H.FLAVOR FROM FIRST_HALF AS H
JOIN JULY AS J 
ON H.FLAVOR = J.FLAVOR
GROUP BY H.FLAVOR
ORDER BY SUM(H.TOTAL_ORDER) DESC
LIMIT 3