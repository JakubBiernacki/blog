import React, { useState } from 'react';
import { Button, Modal, Form, Input } from 'antd';
import { addPost } from '../services';
import Upload from 'antd/es/upload';

const CreatePostForm = ({ visible, onCreate, onCancel, onFile }) => {
  const [form] = Form.useForm();
  return (
    <Modal
      visible={visible}
      title="Utwórz post"
      okText="Utwórz"
      cancelText="Anuluj"
      onCancel={onCancel}
      onOk={() => {
        form
          .validateFields()
          .then(values => {
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
          name="tytul"
          label="Tytuł"
          rules={[{ required: true, message: 'Wpisz tytuł' }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="tresc"
          label="Treść"
          rules={[{ required: true, message: 'Wpisz treść' }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="zdjecia"
          label="Zdjęcie"
          rules={[{ required: false }]}
        >
          <Input onChange={(e) => onFile(e.target.files[0])} type="file"/>
        </Form.Item>
    </Form>
    </Modal>
  );
};

const CreatePost = () => {
  const [visible, setVisible] = useState(false);
  const [file, setFile] = useState();

  const onCreate = async (values) => {
    const dataObj = {
      ...values,
      zdjecia: file,
    };

    const formData = new FormData();
    Object.keys(dataObj).forEach((key) => (
      formData.append(key, dataObj[key])
    ));

    await addPost(formData);
    location.reload();
  };

  return (
    <div>
      <Button
        onClick={() => setVisible(true)}
        type="primary"
      >Utwórz post</Button>
      <CreatePostForm
        visible={visible}
        onCreate={onCreate}
        onFile={setFile}
        onCancel={() => {
          setVisible(false);
        }}
      />
    </div>
  );
};

export default CreatePost;
