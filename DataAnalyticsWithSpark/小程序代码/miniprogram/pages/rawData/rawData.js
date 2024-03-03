const db = wx.cloud.database();

Page({
  /**
   * 页面的初始数据
   */
  data: {
    msg:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getRawData();
  },

  back() {
    wx.navigateBack({
      delta: 0,
    })
  },

  getRawData() {
    var that = this
    db.collection('data0').get({
      success: function(res) {
        that.setData({
          msg: res.data
        })
      }
    })
  }

})