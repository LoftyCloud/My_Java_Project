// home.js
//获取应用实例

const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    term: '',
    currentYearAndMonth: '',
    currentDay: '',
    count: '11483',
    textPart1: '当前分析网购平台：xxx',
    elements: [{
      title: '原始数据',
      name: 'rawData',
      url: 'rawData',
      color: 'blue',
      icon: 'list'
    },
    {
      title: '数据图表',
      name: 'clearData',
      url: 'clearData',
      color: 'cyan',
      icon: 'rank'
    },
    {
      title: '分析结果',
      name: 'result',
      url: 'result',
      color: 'cyan',
      icon: 'form'
    },
    {
      title: '数据说明',
      name: 'info',
      url: 'info',
      color: 'blue',
      icon: 'message'
    }],
    current: 0,  //当前所在页面的 index
    indicatorDots: true, //是否显示面板指示点
    autoplay: true, //是否自动切换
    interval: 3000, //自动切换时间间隔
    duration: 800, //滑动动画时长
    circular: true, //是否采用衔接滑动
    imgUrls: [
      'cloud://cloud1-0gjzbj7z6a6169bd.636c-cloud1-0gjzbj7z6a6169bd-1309578830/轮播图01.png',
      'cloud://cloud1-0gjzbj7z6a6169bd.636c-cloud1-0gjzbj7z6a6169bd-1309578830/轮播图02.png',
      'cloud://cloud1-0gjzbj7z6a6169bd.636c-cloud1-0gjzbj7z6a6169bd-1309578830/轮播图03.png',
      'cloud://cloud1-0gjzbj7z6a6169bd.636c-cloud1-0gjzbj7z6a6169bd-1309578830/轮播图04.png'
    ],
    links:[
      
    ],
    toggleDelay: false
  },
  //轮播图的切换事件
  swiperChange: function(e) {
    this.setData({
      swiperCurrent: e.detail.current
    })
  },
  //点击指示点切换
  chuangEvent: function(e) {
    this.setData({
      swiperCurrent: e.currentTarget.id
    })
  },
  //点击图片触发事件
  swipclick: function(e) {
    
  },
  turnBook() {
    wx.showModal({
      title: '切换失败',
      content: '暂不支持切换！',
      showCancel: false
    })
  },
  //显示日期和还书期限
  onLoad() {
     this.setDate()
  },
  onShow(){
    this.setData({
      count: app.globalData.count
    })
  },
  setDate() {
    var currentDate = new Date()
    var year = currentDate.getFullYear()
    var month = currentDate.getMonth() + 1
    var day = currentDate.getDate()
    this.setData({
      currentYearAndMonth: year+'年'+month+'月',
      currentDay: day+'日'
    }) 
  }
})