import React from "react";
import { render } from "react-dom";
import { ConfigProvider } from 'antd';
import plPL from 'antd/lib/locale/pl_PL';
import App from "./components/App";
import 'antd/dist/antd.css';
import Layout from './layout';
import { BrowserRouter as Router, Switch } from 'react-router-dom';

const Wrapper = () => (
  <ConfigProvider locale={plPL}>
    <Router>
      <Switch>
        <Layout>
          <App />
        </Layout>
      </Switch>
    </Router>
  </ConfigProvider>
);

const appDiv = document.getElementById("app");
render(<Wrapper />, appDiv);
