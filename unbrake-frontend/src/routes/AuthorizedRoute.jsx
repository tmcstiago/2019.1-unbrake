import React from "react";
import PropTypes from "prop-types";
import { Route } from "react-router-dom";
import { Redirect } from "react-router";
import Auth from "../auth/Auth";
import NotAuthorizedRoute from "./NotAuthorizedRoute";

class AuthorizedRoute extends React.PureComponent {
  render() {
    const { superuser, permission } = this.props;

    if (Auth.isSuperuser(superuser) || Auth.hasPermission(permission)) {
      return <Route {...this.props} />;
    }
    if (Auth.isAuthenticated()) {
      return <NotAuthorizedRoute />;
    }
    return <Redirect to="/login" />;
  }
}

AuthorizedRoute.propTypes = {
  superuser: PropTypes.bool,
  permission: PropTypes.string
};

AuthorizedRoute.defaultProps = {
  superuser: false,
  permission: ""
};

export default AuthorizedRoute;
