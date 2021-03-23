import React, { useState } from 'react';
import { Button, Modal, Form, Input, Radio } from 'antd';
import { addComment } from '../services';

const CreateCommentForm = ({ visible, onCreate, onCancel }) => {
  const [form] = Form.useForm();
  return (
    <Modal
      visible={visible}
      title="Dodaj komentarz"
      okText="Dodaj"
      cancelText="Anuluj"
      onCancel={onCancel}
      onOk={() => {
        form
          .validateFields()
          .then(values => {
            form.resetFields();
            onCreate(values);
          })
          .catch(info => {
            console.log('Validate Failed:', info);
          });
      }}
    >
      <Form
        form={form}
        layout="vertical"
        name="form_in_modal"
        initialValues={{ modifier: 'public' }}
      >
        <Form.Item
          name="tresc"
          label="Treść"
          rules={[{ required: true, message: 'Treść komentarza' }]}
        >
          <Input />
        </Form.Item>
      </Form>
    </Modal>
  );
};

const CreateComment = ({ post, rodzic = null }) => {
  const [visible, setVisible] = useState(false);

  const onCreate = async (values) => {
    await addComment({
      ...values,
      post,
      rodzic,
    });

    location.reload();
  };

  return (
    <div>
      <Button
        onClick={() => setVisible(true)}
        type="primary"
      >Dodaj komentarz</Button>
      <CreateCommentForm
        visible={visible}
        onCreate={onCreate}
        onCancel={() => {
          setVisible(false);
        }}
      />
    </div>
  );
};

export default CreateComment;
