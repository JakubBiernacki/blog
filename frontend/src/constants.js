const API_BASE = '/api';

export const loggedIn = (!!localStorage.getItem('loggedIn'));

export const api = {
  posts: {
    all: `${API_BASE}/posty`,
    single: (id) => `${API_BASE}/posty/${id}`,
    comments: (id) => `${API_BASE}/posty/${id}/komentarze`,
    addSingle: `${API_BASE}/posty/`,
  },
  comments: {
    single: (id) => `${API_BASE}/komentarze/${id}`,
    addSingle: `${API_BASE}/kometarze/`,
  },
  users: {
    single: (id) => `${API_BASE}/user/${id}`,
    posts: (id) => `${API_BASE}/user/${id}/posty`,
    profile: (id) => `${API_BASE}/user/${id}/profile`,
  },
  auth: {
    login: `${API_BASE}/user/login/`,
    logout: `${API_BASE}/user/logout`,
    register: `${API_BASE}/user/register/`,
  }
};

export const paths = {
  home: '/',
  auth: {
    login: '/login',
    signUp: '/register',
  },
  post: (id) => `/post/${id}`
};
