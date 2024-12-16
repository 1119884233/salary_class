document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止表单的默认提交行为

    // 获取用户名和密码输入框的值
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // 检查输入是否为空
    if (username === '' || password === '') {
        showError('用户名和密码不能为空');
    } else {
        // 假设用户名和密码是 "admin" 和 "password" 用于演示
        if (username === 'admin' && password === 'password') {
            alert('登录成功！');
            // 这里可以将登录成功后重定向到其他页面
            // window.location.href = 'dashboard.html'; // 例如重定向
        } else {
            showError('用户名或密码错误');
        }
    }
});

function showError(message) {
    var errorMessage = document.getElementById('error-message');
    errorMessage.textContent = message;
    errorMessage.style.display = 'block'; // 显示错误信息
}
