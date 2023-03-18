/*var = khai báo biến  với biến updateBtns là tài liệu "document" 
và getElementsByClassName là trả về tất cả phần từ về 1 tập hợp tên class chỉ định ('update-cart')   */
var updateBtns = document.getElementsByClassName('update-cart')

//phần hoạt động , khi user nhấn "add to cart"*/
// i =0 , i bé hơn độ dài updateBtns , i tăng 1*/
for (i = 0;i < updateBtns.length;i++)
{
    //addEventListener('click') lắng nghe/xem người dùng ấn chuột"click" 
    // function() = hàm gộp những đoạn code lặp lại với biến con 
    updateBtns[i].addEventListener('click', function()
    {
        // biến productId = chính nó set dữ liệu trong Id sản phẩm product(base.html -> home.html ) ->  Product(models.py)
        var productId = this.dataset.product

        // action = chính nó set dữ liệu là 1 hành động
        var action = this.dataset.action
        console.log('productId',productId,'action',action)

        // 'user: ' là string thông báo giống print python
        console.log('user:',user)

        // nếu user là người dùng ẩn danh "AnonymousUser"
        if  (user === "AnonymousUser")
        {
            console.log('user not logged in')
        } 

        else 
        {
            updateUserOrder(productId,action)
        }
    })
}

// định nghĩa cập nhập UserOrder
function updateUserOrder(productId,action)
{
    console.log('user logged in, success add')

    // biến url là lấy đường dẩn của 'update_item/'(urls.py)
    var url = '/update_item/'

    //nhặt url với
    fetch(url,
     {
        method: 'POST',
        headers:
        {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId':productId,'action':action}),
     })

     //response
     .then((response) =>
     {
        return response.json()
     })

     //data xem ngta lấy sản phẩm gì rồi thêm vào giỏ hàng
     //test trong CSDL
     .then((data) =>
     {
        console.log('data',data)




        /** location Trả về true nếu  location bar(url) hiển thị; ngược lại, trả về false. */
        /* reload Xóa trang hiện tại khỏi session history và điều hướng đến URL đã cho. */

        /*Session là một chuỗi các sự kiện người dùng sử dụng trình duyệt để thao tác với 
        website của bạn, từ lúc click chuột vào trang cho đến lúc họ thoát ra khỏi trang của bạn */
        
        /* location.reload() = nếu url hiển thị -> xóa tất cả lịch sử lệnh được ghi lại (của client (data-base trên server giữ nguyên)
        và tải lại trang web mới với dữ liệu hiển thị thay đổi ~ auto update dữ liệu  (với data-base đã được chỉnh sửa lại dựa trên việc client click chuột trước đó) */
        location.reload()
     })
}    
