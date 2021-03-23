import React from "react";
import { Layout, Menu, Breadcrumb, Button, message } from 'antd';
import './layout.css';
import { useHistory } from 'react-router-dom';
import { usePaths } from './utils';
import { logout } from '../services';
import { loggedIn } from '../constants';

const { Header, Content, Footer } = Layout;

const LayoutWrapper = ({ children }) => {
  let history = useHistory();
  const { list: pathsList, selected: selectedPath } = usePaths();
  const menu = pathsList.filter((path) => !path?.hidden).reverse();
  const selectedKey = menu.findIndex(p => p === selectedPath);

  const handleLogout = async () => {
    await logout();
    message.success('Wylogowano');
    localStorage.removeItem('loggedIn');
    location.reload();
  };

  return (
    <Layout className="layout">
      <Header>
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={[selectedKey.toString()]}>
          {menu.map(({ path, text }, index) => (
            <Menu.Item
              onClick={() => history.push(path)}
              key={index.toString()}
            >{text}</Menu.Item>
          ))}
          {loggedIn && (
            <Button style={{ marginLeft: 24 }} onClick={handleLogout} type="primary">Wyloguj</Button>
          )}
        </Menu>
      </Header>
      <Content style={{ padding: '0 50px' }}>
        <Breadcrumb style={{ margin: '16px 0' }}>
          {selectedPath.breadcrumbs.map((breadcrumb) => (
            <Breadcrumb.Item>{breadcrumb}</Breadcrumb.Item>
          ))}
        </Breadcrumb>
        <div className="site-layout-content">{children}</div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>Szymon Dziób Corp. ©2035</Footer>
    </Layout>
  );
};

export default LayoutWrapper;
