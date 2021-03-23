import React from "react";
import { Form, Input, Button, message } from 'antd';
import { useState } from 'react/cjs/react.production.min';
import { signUp } from '../services';

const layout = {
  labelCol: { span: 12 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 12, span: 16 },
};

const Register = () => {
  const [loading, setLoading] = useState(false);

  const onFinish = async (values) => {
    setLoading(true);
    await signUp(values);
    setLoading(false);
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
        label="Adres e-mail"
        name="email"
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

      <Form.Item
        label="Potwórz hasło"
        name="password2"
        rules={[{ required: true, message: 'Potwórz hasło' }]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit" loading={loading} disabled={loading}>
          Zarejestruj się
        </Button>
      </Form.Item>
    </Form>
  );
};

export default Register;
