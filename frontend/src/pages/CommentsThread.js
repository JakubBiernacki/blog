import React from 'react';
import { Button, List } from 'antd';
import Comment from "./Comment";
import CreateComment from './CreateComment';
import { loggedIn } from '../constants';

const CommentsThread = ({ comments, post, rodzic = undefined }) => (
  <List
    itemLayout="horizontal"
    dataSource={comments}
    renderItem={Comment}
    footer={loggedIn ? <CreateComment post={post} rodzic={rodzic} /> : undefined}
  />
);

export default CommentsThread;
