curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer ${LINE_OFFICIAL_TOKEN}' \
-H 'Content-Type: application/json' \
-d \
'{
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": false,
    "name": "index",
    "chatBarText": "呼叫情報員",
    "areas": [
      {
          "bounds": {
              "x": 0,
              "y": 0,
              "width": 834,
              "height": 843
          },
          "action": {
              "type": "message",
              "text": "[選單]校園公車時間表"
          }
      },
      {
          "bounds": {
              "x": 834,
              "y": 0,
              "width": 833,
              "height": 843
          },
          "action": {
              "type": "message",
              "text": "[選單]清華校內工讀"
          }
      },
      {
          "bounds": {
              "x": 1667,
              "y": 0,
              "width": 833,
              "height": 843
          },
          "action": {
              "type": "message",
              "text": "[選單]切換主動推播"
          }
      },
      {
          "bounds": {
              "x": 0,
              "y": 843,
              "width": 834,
              "height": 843
          },
          "action": {
              "type": "message",
              "text": "[選單]校務專區"
          }
      },
      {
          "bounds": {
              "x": 834,
              "y": 843,
              "width": 833,
              "height": 843
          },
          "action": {
              "type": "message",
              "text": "[選單]校園地圖查詢"
          }
      },
      {
          "bounds": {
              "x": 1667,
              "y": 843,
              "width": 833,
              "height": 843
          },
          "action": {
              "type": "message",
              "text": "!"
          }
      }
  ]
}'


curl -v -X POST https://api.line.me/v2/bot/richmenu/richmenu-02fd8dc39fdeb6acb99d6d8f920e3a80/content \
-H "Authorization: Bearer ${LINE_OFFICIAL_TOKEN}" \
-H "Content-Type: image/png" \
-T richmenu-index-vRE.png
