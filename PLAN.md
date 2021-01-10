## 埋点适配计划

- [x] 诸葛 IO
- [x] 神策数据
- [X] GrowingIO 埋点数据
- [ ] 友盟
- [ ] C4J
- [ ] Mixpanel 
- [ ] GA 
- [ ] Ptmind Ptengine
- [ ] 国双 WebDissector
- [ ] 谷歌分析 Google Analytics


## 埋点数据上传API

-  url
    - https://api.growingio.com/v3/{ai}/s2s/cstm?stm={sendingTime}
  
-  request body
    - 单条事件发送
    [      
  {            
    "cs1":"9128391",    
    "tm":1434556935000,    
    "t":"cstm",    
    "n":"BuyProduct",    
    "var":{      
      "product_name":"苹果",      
      "product_classify":"水果",      
      "product_price":14    
    }
  }
]

    - 多条事件发送
    
    [      
  {            
    "cs1":"9128391",    
    "tm":1434556935000,    
    "t":"cstm",    
    "n":"BuyProduct",    
    "var":{      
      "product_name":"苹果",      
      "product_classify":"水果",      
      "product_price":14    
    }
  },   
  {            
    "cs1":"9128391",    
    "tm":1434556935000,    
    "t":"cstm",    
    "n":"BuyProduct",    
    "var":{      
      "product_name":"苹果",      
      "product_classify":"水果",      
      "product_price":14    
    }
  },   
  {            
    "cs1":"9128391",    
    "tm":1434556935000,    
    "t":"cstm",    
    "n":"BuyProduct",    
    "var":{      
      "product_name":"苹果",      
      "product_classify":"水果",      
      "product_price":14    
    }
  }
]