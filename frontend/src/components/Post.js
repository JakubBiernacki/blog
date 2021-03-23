import React from 'react';
import { paths } from '../constants';
import { Avatar, Card } from 'antd';
import dayjs from 'dayjs';
import { Link } from 'react-router-dom';

const { Meta } = Card;

const Post = ({ post, clickable = true }) => {
  const { id, tytul, user, zdjecia, data_utworzenia } = post;

  const content = (
    <Card
      style={{ width: '100%' }}
      cover={<img alt={tytul} src={zdjecia} />}
      hoverable={clickable}
    >
      <Meta
        avatar={<Avatar src={user.image} alt={user.username} />}
        title={tytul}
        description={`${dayjs(data_utworzenia).format("DD.MM.YYYY")} przez ${user.username}`}
      />
    </Card>
  );

  if (!clickable) {
    return content;
  }

  return (
    <Link to={paths.post(id)}>
      {content}
    </Link>
  )
};

export default Post;
