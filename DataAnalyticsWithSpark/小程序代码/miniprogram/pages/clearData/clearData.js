// miniprogram/pages/clearData/clearData.js
import * as echarts from '../../ec-canvas/echarts';
const app = getApp();
let chart = null;

function initChart0(canvas, width, height, dpr) {
  const chart = echarts.init(canvas, null, {
    width: width,
    height: height,
    devicePixelRatio: dpr // new
  });
  canvas.setChart(chart);

  var option = {
    backgroundColor: "#ffffff",
    series: [{
      label: {
        normal: {
          fontSize: 14
        }
      },
      type: 'pie',
      center: ['50%', '50%'],
      radius: ['20%', '40%'],
      data: [{
        value: 13,
        name: '未成年 12.8%'
      }, {
        value: 87,
        name: '成年 87.2%'
      }]
    }]
  };
  chart.setOption(option);
  return chart;
}

function initChart1(canvas, width, height, dpr) {
  chart = echarts.init(canvas, null, {
    width: width,
    height: height,
    devicePixelRatio: dpr // new
  });
  canvas.setChart(chart);

  var option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
      },
      confine: true
    },
    legend: {
      data: ['销量']
    },
    grid: {
      left: 20,
      right: 20,
      bottom: 15,
      top: 40,
      containLabel: true
    },
    xAxis: [
      {
        type: 'value',
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    yAxis: [
      {
        type: 'category',
        axisTick: { show: false },
        data: ['WROGN', 'W', 'Parx', 'Park Avenue', 'Next Look', 'Lavie', 'Indian Terrain','HERE&NOW','Roadster',
        'Puma','Pepe Jeans','Gini and Jony','GAP','Flying Machine','DressBerry','Cortina','Calvin Klein Jeans',
      'AURELIA','U.S. Polo Assn. Kids','Titan','SEJ by Nisha Gupta'],
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    series: [
      {
        name: '销量',
        type: 'bar',
        label: {
          normal: {
            show: true,
            position: 'inside'
          }
        },
        data: [175, 261, 154, 173, 107, 121, 971, 164, 232, 345, 340, 102, 216, 301, 106, 134, 131, 307, 234, 107, 103],
        itemStyle: {
          // emphasis: {
          //   color: '#37a2da'
          // }
        }
      }
    ]
  };

  chart.setOption(option);
  return chart;
}

function initChart2(canvas, width, height, dpr) {
  chart = echarts.init(canvas, null, {
    width: width,
    height: height,
    devicePixelRatio: dpr // new
  });
  canvas.setChart(chart);

  var option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
      },
      confine: true
    },
    legend: {
      data: ['品牌数量', '销量']
    },
    grid: {
      left: 20,
      right: 20,
      bottom: 15,
      top: 40,
      containLabel: true
    },
    xAxis: [
      {
        type: 'value',
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    yAxis: [
      {
        type: 'category',
        axisTick: { show: false },
        data: ['非知名品牌', '知名品牌'],
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    series: [
      {
        name: '品牌数量',
        type: 'bar',
        label: {
          normal: {
            show: true,
            position: 'inside'
          }
        },
        data: [669, 21],
        itemStyle: {
          // emphasis: {
          //   color: '#37a2da'
          // }
        }
      },
      {
        name: '销量',
        type: 'bar',
        label: {
          normal: {
            show: true
          }
        },
        data: [7718, 4784],
        itemStyle: {
          // emphasis: {
          //   color: '#32c5e9'
          // }
        }
      }
    ]
  };

  chart.setOption(option);
  return chart;
}

function initChart3(canvas, width, height, dpr) {
  chart = echarts.init(canvas, null, {
    width: width,
    height: height,
    devicePixelRatio: dpr // new
  });
  canvas.setChart(chart);

  var option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
      },
      confine: true
    },
    legend: {
      data: ['销量']
    },
    grid: {
      left: 20,
      right: 20,
      bottom: 15,
      top: 40,
      containLabel: true
    },
    xAxis: [
      {
        type: 'value',
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    yAxis: [
      {
        type: 'category',
        axisTick: { show: false },
        data: ['button closure','has regular styling','has a polo collar','has a V-neck',
        'has a button-down collar','Red','Blue','button closure','has a V-neck',
      'has a round neck','has regular styling','has unconventional styling','has a polo collar',
    'has a mandarin collar'],
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    series: [
      {
        name: '销量',
        type: 'bar',
        label: {
          normal: {
            show: true,
            position: 'inside'
          }
        },
        data: [62,59,56,56,54,54,120,117,98,98,96,324,277,259],
        itemStyle: {
          // emphasis: {
          //   color: '#37a2da'
          // }
        }
      }
    ]
  };

  chart.setOption(option);
  return chart;
}

function initChart5(canvas, width, height, dpr) {
  const chart = echarts.init(canvas, null, {
    width: width,
    height: height,
    devicePixelRatio: dpr // new
  });
  canvas.setChart(chart);

  var option = {
    backgroundColor: "#ffffff",
    series: [{
      label: {
        normal: {
          fontSize: 14
        }
      },
      type: 'pie',
      center: ['50%', '50%'],
      radius: ['20%', '40%'],
      data: [{
        value: 45,
        name: '男女\n皆宜 \n45.51%'
      }, {
        value: 44,
        name: '女性 \n44.45%'
      }, {
        value: 11,
        name: '男性 11.04%'
      }]
    }]
  };
  chart.setOption(option);
  return chart;
}

function initChart6(canvas, width, height, dpr) {
  const chart = echarts.init(canvas, null, {
    width: width,
    height: height,
    devicePixelRatio: dpr // new
  });
  canvas.setChart(chart);

  var option = {
    backgroundColor: "#ffffff",
    series: [{
      label: {
        normal: {
          fontSize: 14
        }
      },
      type: 'pie',
      center: ['50%', '50%'],
      radius: ['20%', '40%'],
      data: [{
        value: 0.1,
        name: '1张 0.1%'
      }, {
        value: 1.39,
        name: '2张 1.39%'
      }, {
        value: 9.68,
        name: '3张 9.68%'
      }, {
        value: 13.53,
        name: '4张 \n13.53%'
      }, {
        value: 57.13,
        name: '5张 57.13%'
      }, {
        value: 8.64,
        name: '6张 8.64%'
      }, {
        value: 8.46,
        name: '7张 8.46%'
      }, {
        value: 0.81,
        name: '8张 0.81%'
      }, {
        value: 0.19,
        name: '9张 0.19%'
      }, {
        value: 0.02,
        name: '10张 0.02%'
      }]
    }]
  };
  chart.setOption(option);
  return chart;
}

function initChart7(canvas, width, height, dpr) {
  chart = echarts.init(canvas, null, {
    width: width,
    height: height,
    devicePixelRatio: dpr // new
  });
  canvas.setChart(chart);

  var option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
      },
      confine: true
    },
    legend: {
      data: ['销量']
    },
    grid: {
      left: 20,
      right: 20,
      bottom: 15,
      top: 40,
      containLabel: true
    },
    xAxis: [
      {
        type: 'value',
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    yAxis: [
      {
        type: 'category',
        axisTick: { show: false },
        data: ['5000以上','3000-5000','2000-3000','1500-2000',
  '1000-1500','500-1000','0-500'],
        axisLine: {
          lineStyle: {
            color: '#999'
          }
        },
        axisLabel: {
          color: '#666'
        }
      }
    ],
    series: [
      {
        name: '销量',
        type: 'bar',
        label: {
          normal: {
            show: true,
            position: 'inside'
          }
        },
        data: [392,595,824,1204,2411,5659,1396],
        itemStyle: {
          // emphasis: {
          //   color: '#37a2da'
          // }
        }
      }
    ]
  };

  chart.setOption(option);
  return chart;
}

Page({

  data: {
    list: [
      {
        id: 0,
        name: '服装销量-适用年龄与销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart0
            }
          }
        ]
      },
      {
        id: 1,
        name: '服装销量-部分品牌销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart1
            }
          }
        ]
      },
      {
        id: 2,
        name: '服装销量-品牌知名度与销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart2
            }
          }
        ]
      },
      {
        id: 3,
        name: '服装销量-服装样式与销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart3
            }
          }
        ]
      },
      {
        id: 4,
        name: '服装销量-服装关键词与销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart0
            }
          }
        ]
      },
      {
        id: 5,
        name: '服装销量-性别与销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart5
            }
          }
        ]
      },
      {
        id: 6,
        name: '服装销量-图片数量与销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart6
            }
          }
        ]
      },
      {
        id: 7,
        name: '服装销量-价格与销量相关数据',
        open: false,
        options: [
          {
            ec: {
              onInit: initChart7
            }
          }
        ]
      }
    ]
  },
    // 控制抽屉开关
    kindToggle: function (e) {
      var id = e.currentTarget.id, list = this.data.list;
   
      // 使用id获取打开的子列表
      for (var i = 0, len = list.length; i < len; ++i) {
        if (list[i].id == id) {
          list[i].open = !list[i].open
        } else {
          list[i].open = false
        }
      }
      this.setData({
        list: list
      });
    },

  back() {
    wx.navigateBack({
      delta: 0,
    })
  }
})