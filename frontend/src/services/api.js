import { api } from "../constants";
import { message } from 'antd';
import { getCookie } from './getCookie';

const headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-CSRFToken': getCookie('csrftoken')
};

const standardFetch = async (url, options) => fetch(url, { headers, credentials: 'include', ...options })
  .then(r => r.json());

export const getAllPosts = async () => {
  const posts = await standardFetch(api.posts.all);

  return await Promise.all(posts.map(async (post) => ({
    ...post,
    user: await standardFetch(api.users.single(post.user)),
  })));
};

export const getSinglePost = async (id) => {
  let [post, comments] = await Promise.all([
    standardFetch(api.posts.single(id)),
    standardFetch(api.posts.comments(id)),
  ]);

  post.user = await standardFetch(api.users.single(post.user));

  await Promise.all(comments.map(async (comment) => ({
    ...comment,
    user: await standardFetch(api.users.single(comment.user)),
  })));

  comments = comments
    .filter(c => !c.rodzic)
    .map((comment) => {
      const children = comments.filter(({ rodzic }) => rodzic === comment.id);
      return {
        ...comment,
        children,
      };
    });

  return { ...post, comments };
};

const fetchAuthenticated = async (data, url, options = {}) => fetch(url, {
    method: 'POST',
    body: data instanceof FormData ? data : JSON.stringify(data),
    headers,
    credentials: 'same-origin',
    ...options,
  }).then(async (r) => {
    const messages = Object.values(await r.clone().json()).flat();

    if (r.ok) {
      messages.forEach((m) => message.success(m, 2));
      return true;
    } else {
      messages.forEach((e) => message.error(e, 2));
      return false;
    }
});

export const signUp = async (data) => await fetchAuthenticated(data, api.auth.register);

export const login = async (data) => await fetchAuthenticated(data, api.auth.login);

export const logout = async () => await standardFetch(api.auth.logout);

export const addComment = async (data) => await fetchAuthenticated(data, api.comments.addSingle);

export const addPost = async (data) => {
  const { 'Content-Type': cT, ...headersData } = headers;

  return await fetchAuthenticated(data, api.posts.addSingle, {
    headers: headersData
  });
}
