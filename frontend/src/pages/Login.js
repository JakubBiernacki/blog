import React from "react";
import { Form, Input, Button } from 'antd';
import { useState } from 'react/cjs/react.production.min';
import { login } from '../services';

const layout = {
  labelCol: { span: 12 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 12, span: 16 },
};

const Login = () => {
  const [loading, setLoading] = useState(false);

  const onFinish = async (values) => {
    setLoading(true);
    await login(values);
    localStorage.setItem('loggedIn', '1');
    setLoading(false);
    location.reload();
  };

  return (
    <Form
      {...layout}
      name="basic"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      style={{ maxWidth: '400px', margin: 'auto' }}
    >
      <Form.Item
        label="Nazwa użytkownika"
        name="username"
        rules={[{ required: true, message: 'Wpisz nazwę użytkownika' }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Hasło"
        name="password"
        rules={[{ required: true, message: 'Wpisz hasło' }]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit" loading={loading} disabled={loading}>
          Zaloguj się
        </Button>
      </Form.Item>
    </Form>
  );
};

export default Login;
