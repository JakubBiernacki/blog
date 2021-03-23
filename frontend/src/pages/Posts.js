import React from 'react';
import { Spin } from 'antd';
import { getAllPosts } from '../services';
import { useEffect, useState } from 'react/cjs/react.production.min';
import Post from '../components/Post';
import CreatePost from './CreatePost';
import Card from 'antd/es/card';
import { loggedIn } from '../constants';

const Posts = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const getData = async () => {
    setData(await getAllPosts());
    setLoading(false)
  };

  useEffect(() => {
    getData();
  }, [])

  if (loading) {
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
     {loggedIn && (
       <Card>
         <CreatePost />
       </Card>
     )}
     {data.map((post) => (
       <Post post={post} key={post.id} />
     ))}
   </>
 );
};

export default Posts;
