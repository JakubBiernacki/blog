import { loggedIn, paths } from '../constants';
import { useLocation } from "react-router-dom";

const localPaths = [
  {
    path: paths.post(''),
    text: 'Post',
    breadcrumbs: ['Strona główna', 'Post'],
    hidden: true,
  },
  ...(loggedIn ? []:
    [
      {
        path: paths.auth.signUp,
        text: 'Rejestracja',
        breadcrumbs: ['Strona główna', 'Rejestracja']
      },
      {
        path: paths.auth.login,
        text: 'Logowanie',
        breadcrumbs: ['Strona główna', 'Logowanie']
      },
    ]
  ),
  {
    path: paths.home,
    text: 'Strona główna',
    breadcrumbs: ['Strona główna']
  },
];

export const usePaths = () => {
  let location = useLocation();

  return {
    list: localPaths,
    selected: localPaths.find(({ path }) => location.pathname.startsWith(path)),
  }
};
