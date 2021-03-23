import React from 'react';
import { Card, Spin } from 'antd';
import { getSinglePost } from '../services';
import { useEffect, useState } from 'react/cjs/react.production.min';
import { useParams } from "react-router-dom";
import Post from '../components/Post';
import CommentsThread from './CommentsThread';

const Posts = () => {
  const { id } = useParams();
  const [data, setData] = useState();
  const [loading, setLoading] = useState(false);

  const getData = async () => {
    setData(await getSinglePost(id));
    setLoading(false)
  };

  useEffect(() => {
    if (id) {
      getData();
    }
  }, [id])

  if (loading || !data) {
    return (
      <div style={{
        padding: '24px',
        'text-align': 'center',
      }}>
        <Spin />
      </div>
    )
  }

  return (
    <>
      <Post post={data} clickable={false} />
      <Card title="Komentarze" extra={<>Liczba komentarzy:&nbsp;<b>{data.comments.length}</b></>}>
        <CommentsThread comments={data.comments} post={id}/>
      </Card>
    </>
  );
};

export default Posts;
