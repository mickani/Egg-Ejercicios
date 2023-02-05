package com.eggPractica.noticia;

import com.eggPractica.noticia.excepciones.MyException;
import com.eggPractica.noticia.servicios.UsuarioServicio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SeguridadWeb extends WebSecurityConfigurerAdapter{

    @Autowired
    public UsuarioServicio uServicio;
    
    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) throws MyException, Exception{
        auth.userDetailsService(uServicio).passwordEncoder(new BCryptPasswordEncoder());
    }
    
    @Override
    protected void configure(HttpSecurity http)throws Exception{
        http
                .authorizeRequests()
                    .antMatchers("/admin/*").hasRole("ADMIN")
                    .antMatchers("/css/*","/js/*", "/img/*", "/**" )
                    .permitAll()
                .and().formLogin()
                    .loginPage("/login")
                    .loginProcessingUrl("/logincheck")
                    .usernameParameter("nombreUsuario")
                    .passwordParameter("password")
                    .defaultSuccessUrl("/index")
                    .permitAll()
                .and().logout()
                    .logoutUrl("/logout")
                    .logoutSuccessUrl("/")
                    .permitAll()
                .and().csrf().disable();
    }
}
