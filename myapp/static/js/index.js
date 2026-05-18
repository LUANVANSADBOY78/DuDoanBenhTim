// $(function () {
//     let arr_appoint = ['name', 'email', 'phone', 'datepicker', 'timepicker','address', 'service',  'message', 'total']
//     $("#submit").on('click', () => {
//         let data_appoint = {}
//         arr_appoint.forEach(key => {
//             let value = $(`#${key}`).val();
//             data_appoint[key] = value
//         });
//         fetch('/saveAppointment', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(data_appoint)
//         })
//             .then(response => response.json())
//             .then(data => {
//                 Swal.fire({
//                     title: "Đặt lịch thành công",
//                     text: "Vui lòng kiểm tra email",
//                     icon: "success",
//                     confirmButtonText: "OK bro"
//                 });
//                 arr_appoint.forEach(key => {
//                     $(`#${key}`).val('');
//                 });
//                 $("#price-booking").text(`Thành tiền: 0 đ`)
//                 $("#total").val('')
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//             });

//     })
//     $("#login").on('click', () => {
//         let data_login = {
//             'email': $("#email-login").val(),
//             'password': $("#password-login").val(),
//         }
//         fetch('/login', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(data_login)
//         })
//             .then(response => response.json())
//             .then(data => {
//                 Swal.fire({
//                     title: "Đăng nhập thành công",
//                     icon: "success",
//                     confirmButtonText: "OK bro"
//                 }).then((result) => {
//                     /* Read more about isConfirmed, isDenied below */
//                     if (result.isConfirmed) {
//                         document.location.href = '/admin'
//                     }
//                 });

//             })
//             .catch(error => {
//                 console.error('Error:', error);
//             });

//     })
//     $("#submit-feedback").on('click', () => {
//         let data_feedback = {
//             'email': $("#email-feedback").val(),
//             'name': $("#name-feedback").val(),
//             'message': $("#message-feedback").val(),
//             'contentment': $("#contentment-feedback").val(),
//         }
//         console.log(data_feedback);
//         fetch('/saveFeedback', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(data_feedback)
//         })
//             .then(response => response.json())
//             .then(data => {
//                 Swal.fire({
//                     title: "Cảm ơn bạn đã phản hồi",
//                     icon: "success",
//                     confirmButtonText: "OK bro"
//                 })
//                 $("#email-feedback").val('')
//                 $("#name-feedback").val('')
//                 $("#message-feedback").val('')
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//             });
//     })
//     $("#service").on('change',(event)=>{
//         let price =$('option:selected',event.target).data('price');
//         $("#price-booking").text(`Thành tiền: ${price} đ`)
//         $("#total").val(price)
//     })
// })