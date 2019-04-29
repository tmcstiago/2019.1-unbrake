import React from "react";
import PropTypes from "prop-types";
import { Redirect, Route } from "react-router-dom";
import Auth from "../auth/Auth";
import NotAuthorizedRoute from "./NotAuthorizedRoute";

class AuthorizedRoute extends React.PureComponent {
  render() {
    const { superuser } = this.props;

    if (
      Auth.isSuperuser(superuser) // || Auth.hasPermission(permission)
    ) {
      return <Route {...this.props} />;
    }
    if (Auth.isAuthenticated()) {
      return <NotAuthorizedRoute />;
    }
    return (
      <Redirect
        to={{
          pathname: "/login"
        }}
      />
    );
  }
}

AuthorizedRoute.propTypes = {
  superuser: PropTypes.bool
};

AuthorizedRoute.defaultProps = {
  superuser: false
};

export default AuthorizedRoute;
