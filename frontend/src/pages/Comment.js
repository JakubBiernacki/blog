import React from 'react';
import { Avatar, List } from 'antd';
import dayjs from 'dayjs';
import Card from 'antd/es/card';
import CommentsThread from './CommentsThread';

const Comment = ({ tresc, data_utworzenia, user, children, post, id }) => (
  <List.Item>
    <List.Item.Meta
      avatar={<Avatar src={user.image} alt={user.username} />}
      description={dayjs(data_utworzenia).format("DD.MM.YYYY")}
      title={user.username}
    />
    {tresc}
    {children && (
      <Card style={{ marginTop: 24 }}>
        <CommentsThread comments={children} post={post} rodzic={id} />
      </Card>
    )}
  </List.Item>
);

export default Comment;
