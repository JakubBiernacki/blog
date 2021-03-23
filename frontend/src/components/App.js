import React from "react";
import 'antd/dist/antd.css';
import Posts from '../pages/Posts';
import { paths } from '../constants';
import { Route } from 'react-router-dom';
import SinglePost from '../pages/SinglePost';
import Login from '../pages/Login';
import Register from '../pages/Register';

const App = () => (
  <>
    <Route exact path={paths.home}>
      <Posts />
    </Route>
    <Route path={paths.post(':id')}>
      <SinglePost />
    </Route>
    <Route path={paths.auth.login}>
      <Login />
    </Route>
    <Route path={paths.auth.signUp}>
      <Register />
    </Route>
  </>
);

export default App;
